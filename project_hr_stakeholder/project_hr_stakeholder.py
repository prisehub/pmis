# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
<<<<<<< HEAD
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
=======
#              <contact@eficent.com>
>>>>>>> Various corrections
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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


<<<<<<< HEAD
<<<<<<< HEAD
from openerp import tools
from openerp.osv import fields, osv
=======
import tools
from osv import fields, osv
from tools.translate import _
>>>>>>> Various corrections
=======
from openerp import tools
from openerp.osv import fields, orm
from openerp.tools.translate import _
>>>>>>> Preparations for 8.0


class ProjectHrStakeholder(orm.Model):

    _name = "project.hr.stakeholder"
    _description = 'Project Stakeholder'

    def _roles_name_calc(self, cr, uid, ids, name, args, context=None):
        if not ids:
            return []
        res = []

        stakeholders_br = self.browse(cr, uid, ids, context=context)

        for stakeholder in stakeholders_br:
            data = []
            stk_roles = stakeholder.role_ids
            if stk_roles:
                for stk_role in stk_roles:
                    data.insert(0, stk_role.name)
                data.sort(cmp=None, key=None, reverse=False)
                data_str = ', '.join(map(tools.ustr, data))

            else:
                data_str = ''

            res.append((stakeholder.id, data_str))

        return dict(res)

    def _responsibilities_name_calc(
            self, cr, uid, ids, name, args, context=None):

        if not ids:
            return []
        res = []

        stakeholders_br = self.browse(cr, uid, ids, context=context)

        for stakeholder in stakeholders_br:
            data = []
            responsibilities = stakeholder.responsibility_ids
            if responsibilities:
                for responsibility in responsibilities:
                    data.insert(0, responsibility.name)
                data.sort(cmp=None, key=None, reverse=False)
                data_str = ', '.join(map(tools.ustr, data))

            else:
                data_str = ''

            res.append((stakeholder.id, data_str))

<<<<<<< HEAD
    _columns = {        
        
<<<<<<< HEAD
        'name': fields.char('Description', required=True, size=64),
        'partner_id':fields.many2one('res.partner', 'Partner', required=True),
=======
        'name': fields.char('Description', required=False, size=64),
        'partner_id':fields.many2one('res.partner', 'Partner', required=True),              
>>>>>>> Various corrections
=======
        return dict(res)

    _columns = {

<<<<<<< HEAD
        'name': fields.char('Description', required=False, size=64),
        'partner_id': fields.many2one('res.partner', 'Partner', required=True),
>>>>>>> Added group filters on stakeholders
        'project_id': fields.many2one('project.project', 'Project', ondelete='cascade'),

=======
        'name': fields.char(
            'Description',
            required=False,
            size=64
        ),
        'partner_id': fields.many2one(
            'res.partner',
            'Partner',
            required=True
        ),
        'project_id': fields.many2one(
            'project.project',
            'Project',
            ondelete='cascade'
        ),
>>>>>>> * make the prices fields visible on resource plan
        'role_ids': fields.many2many(
            'project.hr.role',
            'stakeholder_role_rel',
            'stakeholder_id',
            'role_id',
            'Roles',
            help="The assignment of the roles and responsibilities determines "
                 "what actions the project manager, project team member, or "
                 "individual contributor will have in the project. Roles and "
                 "responsibilities generally support the project scope since "
                 "this is the required work for the project."
        ),
        'responsibility_ids': fields.many2many(
            'project.hr.responsibility',
            'stakeholder_responsibility_rel',
            'stakeholder_id',
            'responsibility_id',
            'Responsibilities',
            help="The assignment of the roles and responsibilities determines "
                 "what actions the project manager, project team member, or "
                 "individual contributor will have in the project. Roles and "
                 "responsibilities generally support the project scope since "
                 "this is the required work for the project."
        ),
        'roles_name_str': fields.function(
            _roles_name_calc,
            method=True,
            type='text',
            string='Roles',
            help='Project Stakeholder roles'
        ),
        'responsibilities_name_str': fields.function(
            _responsibilities_name_calc,
            method=True,
            type='text',
            string='Responsibilities',
            help='Project Stakeholder responsibilities'
        ),

        'influence': fields.text(
            'Influence'
        ),
    }

    def name_get(self, cr, uid, ids, context=None):
        if context is None:
            context = {}
        if not ids:
            return []
        res = []
        for stakeholder in self.browse(cr, uid, ids, context=context):
            stakeholder_name = ""
            if stakeholder.partner_id:
                stakeholder_name = stakeholder.partner_id.name
            res.append((stakeholder.id, stakeholder_name))
        return res
