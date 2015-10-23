{
    "name": "Project Stakeholder Management",
    "version": "10.0.2.0.7",
    "author": "Eficent, " "Matmoz d.o.o., " "Project Expert Team",
    "contributors": [
        "Jordi Ballester <jordi.ballester@eficent.com>",
        "Matjaž Mozetič <m.mozetic@matmoz.si>",
        "Cristian Salamea <cs@prisehub.com>",
    ],
    "website": "http://project.expert",
    "category": "Project Management",
    "license": "AGPL-3",
    "depends": ["analytic_plan", "project_charter"],
    "data": [
        "security/ir.model.access.csv",
        "security/project_security.xml",
        "data/project_hr_stakeholder_data.xml",
        "views/project_hr_role.xml",
        "views/project_hr_responsibility.xml",
        "views/project_hr_stakeholder.xml",
        "views/project_view.xml",
    ],
    "installable": True,
    "active": False,
}