from odoo import fields, models


class ProjectHrResponsibility(models.Model):

    _name = "project.hr.responsibility"
    _description = "Project Responsibility"

    code = fields.Char("Code", size=4, required=True)
    name = fields.Char("Name", size=128, required=True, translate=True)
    description = fields.Text("Description", translate=True)
