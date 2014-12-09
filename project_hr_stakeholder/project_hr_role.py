# -*- coding: utf-8 -*-
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
=======
#              <contact@eficent.com>
>>>>>>> Various corrections
=======
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
>>>>>>> New revision
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
<<<<<<< HEAD
<<<<<<< HEAD
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
from openerp import fields, models
from openerp.tools.translate import _
>>>>>>> Preparations for 8.0


class ProjectHrRole(models.Model):

    _name = "project.hr.role"
    _description = 'Project Role'

    code = fields.Char('Code', size=4, required=True)
    name = fields.Char('Name', size=128, required=True, translate=True)
    description = fields.Text('Description', translate=True)
=======
import tools
from osv import fields, osv
from tools.translate import _
=======
from openerp.osv import fields, osv
>>>>>>> Updated the imports to work with v8.  Removed a lot in the process.
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

    
class project_hr_role(osv.osv):
    
    _name = "project.hr.role"
    _description = 'Project Role'
    
    _columns = {        
        'code': fields.char('Code', size=4, required=True),
        'name': fields.char('Name', size=128, required=True, translate=True),
        'description': fields.text('Description', translate=True),                                         
    }
    

project_hr_role()

<<<<<<< HEAD
>>>>>>> New revision
=======
>>>>>>> Various corrections
