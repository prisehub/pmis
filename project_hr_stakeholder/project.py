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
from openerp.osv import fields, osv
=======
import tools
from osv import fields, osv
from tools.translate import _
>>>>>>> Various corrections
=======
from openerp import tools
from openerp.osv import fields, osv
from openerp.tools.translate import _
>>>>>>> Preparations for 8.0


<<<<<<< HEAD:project_hr_stakeholder/project.py
class project(osv.osv):
    _name = "project.project"
    _inherit = "project.project"

    _columns = {
        'stakeholder_ids': fields.one2many(
            'project.hr.stakeholder',
            'project_id',
            'Stakeholders'
        ),
    }

project()
=======
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
>>>>>>> Pep-8 spring cleaning!!!!!:project_hr_stakeholder/__init__.py
