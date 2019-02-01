from odoo import fields, models


class ProjectHrStakeholder(models.Model):

    _name = "project.hr.stakeholder"
    _description = "Project Stakeholder"

    name = fields.Char("Description", size=64)
    # partner_id = fields.Many2one("res.partner", "Partner", required=True)
    partnerd_id = fields.Many2one("res.partner", "Partner", required=True)
    project_id = fields.Many2one("project.project", "Project", ondelete="cascade")
    role_ids = fields.Many2many(
        "project.hr.role",
        string="Roles",
        help="The assignment of the roles and responsibilities determines "
        "what actions the project manager, project team member, or "
        "individual contributor will have in the project. Roles and "
        "responsibilities generally support the project scope since "
        "this is the required work for the project.",
    )
    responsibility_ids = fields.Many2many(
        "project.hr.responsibility",
        string="Responsibilities",
        help="The assignment of the roles and responsibilities determines "
        "what actions the project manager, project team member, or "
        "individual contributor will have in the project. Roles and "
        "responsibilities generally support the project scope since "
        "this is the required work for the project.",
    )
    influence = fields.Text("Influence")

    def name_get(self):
        res = []
        for stakeholder in self:
            stakeholder_name = ""
            if stakeholder.partnerd_id:
                stakeholder_name = stakeholder.partnerd_id.name
            res.append((stakeholder.id, stakeholder_name))
        return res
