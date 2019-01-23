from odoo import fields, models


class ProjectHrRole(models.Model):

    _name = "project.hr.role"
    _description = "Project Role"

    code = fields.Char("Code", size=4, required=True)
    name = fields.Char("Name", size=128, required=True, translate=True)
    description = fields.Text("Description", translate=True)
