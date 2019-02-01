from odoo import fields, models


class ProjectProject(models.Model):
    _inherit = "project.project"

    stakeholder_ids = fields.One2many(
        "project.hr.stakeholder", "project_id", string="Stakeholders"
    )
