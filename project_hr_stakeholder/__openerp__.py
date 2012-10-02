# -*- coding: utf-8 -*-
<<<<<<< HEAD

{
<<<<<<< HEAD
<<<<<<< HEAD
    "name": "Project Stakeholder management",
    "version": "1.0",
    "author": "Eficent",
    "website": "http://www.eficent.com",
=======
    "name": "Project Stakeholder Management",
    "version": "2.0.6",
    "author": "Eficent",
    "website": "",
>>>>>>> Various corrections
    "category": "Generic Modules/Projects & Services",
    "depends": [
        "base",
        "project",
        "analytic_plan",
        "project_charter"
=======
    'name': 'Project Stakeholder Management',
    'version': '8.0.2.0.9',
    'author': 'Eficent, '
              'Matmoz d.o.o., '
              'Project Expert Team',
    'contributors': [
        'Jordi Ballester <jordi.ballester@eficent.com>',
        'Matjaž Mozetič <m.mozetic@matmoz.si>',
>>>>>>> Fixes
    ],
<<<<<<< HEAD
    "description": """
This module offers the possibility to register at project level the stakeholders involved in a project.
    - It adds a 'Stakeholders' tab in the project form.
    - The stakeholder can be registered as a partner, or a contact person.
    - You can specify the roles and responsibilities of the stakeholders in this project.
    - You can maintain a master data for roles and responsibilities.
    """,
    "data": [
        "project_hr_role.xml",
        "project_hr_responsibility.xml",
<<<<<<< HEAD
        "project_hr_stakeholder.xml",        
=======
        "project_hr_stakeholder.xml",
>>>>>>> Various corrections
=======
##############################################################################
#
#    Copyright (C) 2011 Eficent (<http://www.eficent.com/>)
#              Jordi Ballester Alomar <jordi.ballester@eficent.com>
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


{
    "name": "Project Management",
    "version": "1.0",
    "author": "Jordi Ballester (Eficent)",
    "website": "http://www.eficent.com",
    "category": "Generic Modules/Projects & Services",
    "depends": [
                "base",
                "project",                       
                ],
    "description": """ This module offers the possibility to register at project level the stakeholders involved in a project.
        - It adds a 'Stakeholders' tab in the project form.
        - The stakeholder can be registered as a partner, or a contact person. 
        - You can specify the roles and responsibilities of the stakeholders in this project.
        - You can maintain a master data for roles and responsibilities.
    """,
    "init_xml": [
                ],
    "update_xml": [    
        "project_hr_role.xml",
        "project_hr_responsibility.xml",
        "project_hr_stakeholder.xml",        
>>>>>>> New revision
        "project_view.xml",
        "security/ir.model.access.csv",
        "security/project_security.xml",
        "project_hr_stakeholder_data.xml",
<<<<<<< HEAD
=======
    'website': 'http://project.expert',
    'category': 'Advanced Project Management',
    'license': 'AGPL-3',
    'depends': [
        'base',
        'project',
        'analytic_plan',
        'project_charter'
    ],
    'data': [
        'project_hr_role.xml',
        'project_hr_responsibility.xml',
        'project_hr_stakeholder.xml',
        'project_view.xml',
        'security/ir.model.access.csv',
        'security/project_security.xml',
        'project_hr_stakeholder_data.xml',
>>>>>>> Enhance the module descriptions
    ],
    'demo': [

    ],
    'test': [
=======
    ],
    'demo_xml': [

    ],
    'test':[
>>>>>>> New revision
    ],
    'installable': True,
    'active': False,
    'certificate': '',
}
<<<<<<< HEAD
=======
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
>>>>>>> New revision
