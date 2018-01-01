# -*- coding: utf-8 -*-

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
        "project_view.xml",
        "security/ir.model.access.csv",
        "security/project_security.xml",
        "project_hr_stakeholder_data.xml",
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
    ],
    'installable': True,
    'active': False,
    'certificate': '',
}
