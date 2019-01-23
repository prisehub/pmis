# © 2015 MATMOZ d.o.o. - Matjaž Mozetič
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl.html).

from odoo import models, fields


class Project(models.Model):

    _inherit = "project.project"

    notes = fields.Text("Notes")
    project_outscope_ids = fields.One2many("project.outscope", "project_id")
    project_success_ids = fields.One2many("project.success", "project_id")
    project_constraints_ids = fields.One2many("project.constraints", "project_id")


class ProjectOutscope(models.Model):
    """Out of scope"""

    _name = "project.outscope"
    _description = __doc__

    project_id = fields.Many2one("project.project", string="Projects")
    out_scope = fields.Text(
        "Out of Scope",
        help="""
It is just as important to agree on what is OUT OF SCOPE as it
is to define what is IN SCOPE as stakeholders will often have
different ideas regarding what is supposed to be IN the
project and what IS NOT. Obtain agreement up front to avoid
unnecessary disputes later on.
This is a useful task to conduct with key stakeholders and
can help clarify issues at any time in the Initiation or
Planning Phases.
Examples of areas that could be examined and clarified
include:

* The type of deliverables that are in scope and out of scope
* The major life-cycle processes that are in scope and out of
   scope
* The types of data that are in scope and out of scope
* The data sources that are in scope or out of scope
* The organisations that are in scope and out of scope
* The major functionality that is in scope and out of scope
        """,
    )


class Success(models.Model):
    """Success"""

    _name = "project.success"
    _description = __doc__

    project_id = fields.Many2one("project.project", string="Projects")
    success = fields.Text(
        "Criteria",
        help="""
PROJECT OBJECTIVES
The success of your project will be defined by how well you
meet your objectives. The more explicitly you state your
objectives at the outset, the less disagreement there will
be at the end about whether you have met them. Remember
that at this early stage of the project, there are still
many “unknown factors”. Be prepared to revise your
objectives as you gather more information about what you
need to achieve.

WRITING PROJECT OBJECTIVES
Project objectives are concrete statements that describe
what the project is trying to achieve. Objectives should
be developed for time, cost, quality (or functionality)
and should:

* Be aligned to business objectives
* Be measurable
* Be achievable
* Be consistent
* Be readily understandable
* Be few in number
* Have the full support and commitment of key stakeholders

Examples:
* Maximum Deadline on ...
* Maximum Budget = ...
        """,
    )


class ProjectConstraint(models.Model):
    """Constraints"""

    _name = "project.constraints"
    _description = __doc__

    project_id = fields.Many2one("project.project", string="Projects")
    constraints = fields.Text(
        string="Constraints",
        help="""
Project constraints are known facts that will influence how
the project is planned and managed. A constraint is a given
factor that is outside of the project planner’s scope of
control, which unless it is lifted or otherwise removed, will
force project actions to work around it.
        """,
    )
