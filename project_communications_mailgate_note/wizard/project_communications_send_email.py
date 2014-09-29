# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

from openerp.osv import osv, fields
from openerp.tools.translate import _
import base64
import itertools
from openerp import tools
import re


AVAILABLE_STATES = [('unchanged', 'Unchanged'),('draft', 'Draft'),('open', 'In Progress'),('pending', 'Pending'), ('cancelled', 'Cancelled'), ('close', 'Close')]


class project_send_new_email_attachment(osv.osv_memory):
    _name = 'project.send.mail.attachment'

    _columns = {
        'binary' : fields.binary('Attachment', required=True),
        'name' : fields.char('Name', size=128, required=True),
        'wizard_id' : fields.many2one('crm.send.mail', 'Wizard', required=True),
    }
    
    

project_send_new_email_attachment()

class project_send_new_email(osv.osv_memory):
    """ Sends new email for the case"""
    _name = "project.send.mail"
    _description = "Send new email"

    _columns = {
        'email_to' : fields.char('To', size=512, required=True),
        'email_from' : fields.char('From', size=128, required=True),
        'reply_to' : fields.char('Reply To', size=128, required=True, help="Reply-to of the Sales team defined on this case"),
        'email_cc' : fields.char('CC', size=512, help="These addresses will receive a copy of this email. To modify the permanent CC list, edit the global CC field of this case"),
        'subject': fields.char('Subject', size=512, required=True),
        'body': fields.text('Message Body', required=True),
        'state': fields.selection(AVAILABLE_STATES, string='Set New State To', required=True),
        'attachment_ids' : fields.one2many('crm.send.mail.attachment', 'wizard_id'),
        'html': fields.boolean('HTML formatting?', help="Select this if you want to send email with HTML formatting."),
    }


    def action_send(self, cr, uid, ids, context=None):
        """ This sends an email to ALL the addresses of the selected partners.
        """
        hist_obj = self.pool.get('mailgate.message')

        if context is None:
            context = {}

        if not context.get('active_model'):
            raise osv.except_osv(_('Error'), _('Can not send mail!'))

        model = context.get('active_model')
        case_pool = self.pool.get(model)
        res_id = context and context.get('active_id', False) or False

        for obj in self.browse(cr, uid, ids, context=context):
            attach = [
                (x.name, base64.decodestring(x.binary)) for x in obj.attachment_ids
            ]

            subtype = 'plain'
            message_id = None
            ref_id = None

            case = case_pool.browse(cr, uid, res_id, context=context)
            if context.get('mail', 'new') == 'new':
                if case.message_ids:
                    message_id = case.message_ids[0].message_id
            elif context.get('mail') == 'forward':
                # extract attachements from case and emails according to mode
                attachments = []
                attach_pool = self.pool.get('ir.attachment')
                direct_attachments = attach_pool.search(cr, uid, [('res_model', '=', 'crm.lead'), ('res_id', '=', res_id)], context=context)
                attachments += attach_pool.browse(cr, uid, direct_attachments, context=context)
                if obj.history in ['latest', 'whole'] and case.message_ids:
                    msgs = case.message_ids
                    if obj.history == 'latest':
                        msgs = msgs[:1]
                    attachments.extend(itertools.chain(*[m.attachment_ids for m in msgs]))
                attach_all = [(a.datas_fname or a.name, base64.decodestring(a.datas)) for a in attachments if a.datas]
                attach += attach_all

            else:
                hist = hist_obj.browse(cr, uid, res_id, context=context)
                message_id = hist.message_id
                model = hist.model
                case_pool = self.pool.get(model)
                res_id = hist.res_id
                ref_id = hist.ref_id
                case = case_pool.browse(cr, uid, res_id, context=context)
            emails = re.findall(r'([^ ,<@]+@[^> ,]+)', obj.email_to or '')
            email_cc = re.findall(r'([^ ,<@]+@[^> ,]+)', obj.email_cc or '')
            emails = filter(None, emails)
            body = obj.body

            body = body and tools.ustr(body) or ''
            email_from = getattr(obj, 'email_from', False)
            x_headers = {}
            if message_id:
                x_headers['References'] = "%s" % (message_id)

            if obj.html:
                subtype = 'html'

            flag = tools.email_send(
                email_from,
                emails,
                obj.subject,
                body,
                email_cc=email_cc,
                attach=attach,
                subtype=subtype,
                reply_to=obj.reply_to,
                openobject_id=str(case.id),
                x_headers=x_headers
            )

            if not flag:
                raise osv.except_osv(_('Error!'), _('Unable to send mail. Please check SMTP is configured properly.'))

            msg_dict = {'new': 'Send', 'reply': 'Reply', 'forward': 'Forward'}
            case_pool.history(cr, uid, [case], _(msg_dict[context.get('mail', 'new')]), history=True, \
                            email=obj.email_to, details=body, \
                            subject=obj.subject, email_from=email_from, \
                            email_cc=', '.join(email_cc), message_id=message_id, \
                            references=ref_id or message_id, attach=attach)
            if obj.state == 'unchanged':
                pass
            elif obj.state == 'done':
                case_pool.do_close(cr, uid, [case.id])
            elif obj.state in ['draft', 'cancel', 'open', 'pending']:
                act = 'do_' + obj.state
                getattr(case_pool, act)(cr, uid, [case.id])

        return {'type': 'ir.actions.act_window_close'}

    def default_get(self, cr, uid, fields, context=None):
        """
        This function gets default values
        """
        if context is None:
            context = {}

        if not context.get('active_model'):
            raise osv.except_osv(_('Error'), _('Can not send mail!'))

        res = super(project_send_new_email, self).default_get(cr, uid, fields, context=context)

        if context.get('mail') == 'reply':
            res.update(self.get_reply_defaults(cr, uid, fields, context=context))
            return res

        model = context.get('active_model')
        mod_obj = self.pool.get(model)
        res_id = context and context.get('active_ids', []) or []

        user_obj = self.pool.get('res.users')
        user_mail_from = user_obj._get_email_from(cr, uid, [uid], context=context)[uid]


        for case in mod_obj.browse(cr, uid, res_id, context=context):
            if 'email_to' in fields:
                user_mail_to = ''
                if case.members:
                    for member in case.members:
                        if not user_mail_to :
                            user_mail_to = user_obj._get_email_from(cr, uid, [member.id], context=context)[member.id]
                        else:
                            user_mail_to += ', ' + user_obj._get_email_from(cr, uid, [member.id], context=context)[member.id]
                res.update({'email_to': user_mail_to and tools.ustr(user_mail_to) or ''})
            if 'email_from' in fields:
                res.update({'email_from': user_mail_from and tools.ustr(user_mail_from) or ''})
            if 'subject' in fields:
                if case:
                    subject = '[' + case.complete_name + '] '
                else:
                    subject = case.name
                res.update({'subject': tools.ustr(context.get('subject', subject) or '')})
            if 'email_cc' in fields:
                user_mail_cc = ''
                if case:
                    user_mail_cc = user_obj._get_email_from(cr, uid, [case.user_id.id], context=context)[case.user_id.id]
                res.update({'email_cc':  user_mail_cc and tools.ustr(user_mail_cc) or ''})
            if 'body' in fields:
                res.update({'body': u'\n'+(tools.ustr(case.user_id.signature or ''))})
            if 'state' in fields:
                res.update({'state': u'pending'})

        return res

    def get_reply_defaults(self, cr, uid, fields, context=None):
        """
        This function gets default values for reply mail
        """
        hist_obj = self.pool.get('mailgate.message')
        res_ids = context and context.get('active_ids', []) or []

        user_obj = self.pool.get('res.users')
        user_mail_from = user_obj._get_email_from(cr, uid, [uid], context=context)[uid]

        include_original = context and context.get('include_original', False) or False
        res = {}
        for hist in hist_obj.browse(cr, uid, res_ids, context=context):
            model = hist.model

            # In the case where the project does not exist in the database
            if not model:
                return {'type': 'ir.actions.act_window_close'}

            model_pool = self.pool.get(model)
            res_id = hist.res_id
            case = model_pool.browse(cr, uid, res_id)
            if 'email_to' in fields:
                user_mail_to = ''
                if case and case.members:
                    for member in case.members:
                        if not user_mail_to :
                            user_mail_to = user_obj._get_email_from(cr, uid, [member.id], context=context)[member.id]
                        else:
                            user_mail_to += ', ' + user_obj._get_email_from(cr, uid, [member.id], context=context)[member.id]
                res.update({'email_to': user_mail_to and tools.ustr(user_mail_to) or ''})
            if 'email_from' in fields:
                res.update({'email_from': user_mail_from and tools.ustr(user_mail_from) or False})

            signature = u'\n' + (tools.ustr(case.user_id.signature or '')) + u'\n'
            original = [signature]

            if include_original == True and 'body' in fields:
                header = u'-------- Original Message --------'
                sender = u'From: %s' %(tools.ustr(hist.email_from or ''))
                to = u'To: %s' % (tools.ustr(hist.email_to or ''))
                sentdate = u'Date: %s' % (tools.ustr(hist.date))
                desc = u'\n%s'%(tools.ustr(hist.description))

                original = [signature, header, sender, to, sentdate, desc]

            res['body']= u'\n' + u'\n'.join(original)

            if 'subject' in fields:
                res.update({u'subject': u'Re: %s' %(tools.ustr(hist.name or ''))})
            if 'email_cc' in fields:
                user_mail_cc = ''
                if case:
                    user_mail_cc = user_obj._get_email_from(cr, uid, [case.user_id.id], context=context)[case.user_id.id]
                res.update({'email_cc':  user_mail_cc and tools.ustr(user_mail_cc) or ''})
            if 'state' in fields:
                res['state'] = u'pending'
        return res

    def view_init(self, cr, uid, fields_list, context=None):
        """
        This function checks for precondition before wizard executes
        @param self: The object pointer
        @param cr: the current row, from the database cursor,
        @param uid: the current user’s ID for security checks,
        @param fields: List of fields for default value
        @param context: A standard dictionary for contextual values

        """
        if context is None:
            context = {}

        if not context.get('active_model'):
            raise osv.except_osv(_('Error'), _('Can not send mail!'))
        return True

project_send_new_email()

