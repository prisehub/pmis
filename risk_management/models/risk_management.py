# -*- coding: utf-8 -*-
# Copyright (C) 2011-2015 ValueDecision Ltd <http://www.valuedecision.com>.
# Copyright (C) 2015 Neova Health <http://www.neovahealth.co.uk>.
# Copyright (C) 2015 Matmoz d.o.o. <http://www.matmoz.si>.
# Copyright (C) 2017 Luxim d.o.o. <http://www.luxim.si>.
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

import logging

from odoo import models, fields, api
from datetime import date

_logger = logging.getLogger(__name__)


class RiskManagementRiskCategory(models.Model):
    _name = "risk.management.category"
    _description = "Risk log category table"

    name = fields.Char(string="Risk Category", size=64, required=True)


class RiskManagementRiskResponseCategory(models.Model):
    _name = "risk.management.response.category"
    _description = "Risk log response category table"

    type = fields.Selection(
        [("threat", "Threat"), ("opportunity", "Opportunity")], "Type"
    )
    name = fields.Char(string="Response Category", size=64, required=True)


class RiskManagementProximity(models.Model):
    _name = "risk.management.proximity"
    _description = "Risk log proximity table"

    name = fields.Char(string="Proximity", size=64, required=True)


class RiskManagementRisk(models.Model):
    _name = "risk.management.risk"
    _description = "Risk"
    _inherit = ["mail.thread"]

    _TRACK = {
        "draft": "risk_management.mt_risk_draft",
        "active": "risk_management.mt_risk_active",
        "closed": "risk_management.mt_risk_closed",
    }

    def _track_subtype(self, init_values):
        self.ensure_one()
        if "state" in init_values:
            return self._TRACK[self.state]
        return super(RiskManagementRisk, self)._track_subtype(init_values)

    @api.depends("risk_response_ids")
    def _risk_response_count(self):
        for record in self:
            record.risk_response_count = len(record.risk_response_ids)

    @api.depends("impact_inherent", "probability_inherent")
    def _calculate_expected_inherent_value(self):
        for record in self:
            record.expected_value_inherent = (
                record.impact_inherent * record.probability_inherent
            )

    @api.depends("impact_residual", "probability_residual")
    def _calculate_expected_residual_value(self):
        for record in self:
            record.expected_value_residual = (
                record.impact_residual * record.probability_residual
            )

    @api.one
    def set_state_draft(self):
        return self.write({"state": "draft"})

    @api.one
    def set_state_active(self):
        return self.write({"state": "active"})

    @api.one
    def set_state_closed(self):
        return self.write({"state": "closed"})

    # ##### define Risk code #####  #

    @api.model
    def create(self, vals):
        if vals.get("name", "/"):
            vals["name"] = self.env["ir.sequence"].get("risk.management.risk")
        return super(RiskManagementRisk, self).create(vals)

    @api.multi
    def copy(self, default=None):
        self.ensure_one()
        if default is None:
            default = {}
        default["name"] = self.env["ir.sequence"].get("risk.management.risk")
        return super(RiskManagementRisk, self).copy(default)

    name = fields.Char(
        "Risk Id",
        size=64,
        required=True,
        readonly=True,
        default="/",
        states={"draft": [("readonly", False)]},
        select=True,
        help="""
Risk label. Can be changed as long as risk is in state 'draft'.
""",
    )
    description = fields.Char(
        string="Risk Description",
        size=64,
        help="""
Short description of the Risk.

Project risks are characteristics, circumstances or
features of the project environment that may have an
adverse effect on the project or the quality of the
deliverables.

Project assumptions are knowledge about the project
that is taken as being true or correct for the purpose
of project planning. Assumptions are made to allow
planning to proceed with limited information about
certain elements that are vital to the management of
the project. Assumptions must be tested prior to
finalising the Project Plan.
""",
    )
    project_id = fields.Many2one("project.project", "Project", required=True)
    author_id = fields.Many2one(
        "res.users", "Author", required=True, default=lambda self: self.env.user.id
    )
    color = fields.Integer("Color", default=0)
    date_registered = fields.Date(
        "Date Registered",
        required=True,
        default=lambda *a: date.today().strftime("%Y-%m-%d"),
        help="Date of the Risk registered. Auto populated.",
    )
    date_modified = fields.Date("Date Modified", help="Date of last update.")
    risk_category_id = fields.Many2one(
        "risk.management.category",
        "Risk Category",
        required=True,
        help="""
Risk Category: The type of risk in terms of the project's or business' chosen
categories (e.g. Schedule, quality, legal etc.)
""",
    )
    description_cause = fields.Text("Cause")
    description_event = fields.Text("Event")
    description_effect = fields.Text("Effect")
    impact_inherent = fields.Integer(
        "Inherent Impact",
        required=True,
        default=0,
        help="""
Impact: The result of a particular threat or opportunity actually occurring,
or the anticipation of such a result. This is the pre-response value, common
used scales are 1 to 10 or 1 to 100.
""",
    )
    impact_residual = fields.Integer(
        "Residual Impact",
        required=True,
        default=0,
        help="""
Impact: The result of a particular threat or opportunity actually occurring,
or the anticipation of such a result. This is the post-response value, common
used scales are 1 to 10 or 1 to 100.
""",
    )
    probability_inherent = fields.Integer(
        "Inherent Probability",
        required=True,
        default=0,
        help="""
Probability: The evaluated likelihood of a particular threat or opportunity
actually happening, including a consideration of the frequency with which this
may arise. This is the pre-response value, common used scales are 1 to 10
or 1 to 100.
""",
    )
    probability_residual = fields.Integer(
        "Residual Probability",
        required=True,
        default=0,
        help="""
Probability: The evaluated likelihood of a particular threat or opportunity
actually happening, including a consideration of the frequency with which this
may arise. This is the post-response value, common used scales are 1 to 10
or 1 to 100.
""",
    )
    expected_value_inherent = fields.Float(
        compute="_calculate_expected_inherent_value",
        method=True,
        string="Expected Inherent Value",
        store=True,
        help="""
Expected Value. Cost of inherent impact * inherent probability. This is the
pre-response value.
""",
    )
    expected_value_residual = fields.Float(
        compute="_calculate_expected_residual_value",
        method=True,
        string="Expected Residual Value",
        store=True,
        help="""
Expected Value. Cost of residual impact * residual probability. This is the
post-response value.
""",
    )
    proximity_id = fields.Many2one(
        "risk.management.proximity",
        "Proximity",
        help="""
Proximity: This would typically state how close to the present time the risk
event is anticipated to happen (e.g. for project risks Imminent, within stage,
within project, beyond project). Proximity should be recorded in accordance
with the project's chosen scales or business continuity time scales.
""",
    )
    risk_response_category_id = fields.Many2one(
        "risk.management.response.category",
        "Response Category",
        help="""
Risk Response Categories: How the project will treat the risk in terms of
the project's (or business continuity planning) chosen categories.
""",
    )
    risk_response_ids = fields.One2many("project.task", "risk_id", "Response Ids")
    risk_response_count = fields.Integer(compute="_risk_response_count", type="integer")
    state = fields.Selection(
        selection="_get_states",
        string="State",
        readonly=True,
        default="draft",
        help="""
A risk can have one of these three states: draft, active, closed.
""",
        track_visibility="onchange",
    )
    risk_owner_id = fields.Many2one(
        "res.users",
        "Owner",
        help="""
Risk Owner: The person responsible for managing the risk (there can be only
one risk owner per risk), risk ownership is assigned to a managerial level,
in case of business continuity to a C-level manager.
""",
    )

    company_id = fields.Many2one(
        "res.company",
        string="Company",
        required=True,
        readonly=True,
        states={"draft": [("readonly", False)]},
        default=lambda self: self.env.user.company_id.id,
    )

    @api.model
    def _get_states(self):
        states = [("draft", "Draft"), ("active", "Confirmed"), ("closed", "Closed")]
        return states

    @api.multi
    def _subscribe_extra_followers(self, vals):
        user_ids = [
            vals[x]
            for x in ["author_id", "risk_owner_id"]
            if x in vals
            if not vals[x] is False
        ]
        if len(user_ids) > 0:
            self.message_subscribe_users(user_ids=user_ids)

        risks = self.read(["message_follower_ids", "risk_response_ids"])
        for risk in risks:
            if "risk_response_ids" in risk and risk["risk_response_ids"]:
                task_ob = self.env("project.task")
                task_ob.message_subscribe(
                    risk["risk_response_ids"], risk["message_follower_ids"]
                )

    @api.multi
    def write(self, vals):
        ret = super(RiskManagementRisk, self).write(vals)
        self._subscribe_extra_followers(vals)
        return ret
