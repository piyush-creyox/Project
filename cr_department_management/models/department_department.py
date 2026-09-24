from odoo import models, fields, api


class Department(models.Model):
    _name = "department.department"
    _description = "department.department"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name", required = True)
    code = fields.Char("Code")

    no_of_students = fields.Integer(
        "No_Of_Students",
        compute='_compute_no_of_students'
    )
    staff_ids = fields.Many2many('employee.employee')

    hod_id = fields.Many2one(
        'employee.employee',
        string='HOD',
        domain=[('is_hod', '=', True)]
    )

    student_ids = fields.One2many(
        'student.student',
        "department_id",
        domain=[('type', '=', 'internal')]
    )

    notes = fields.Html("Notes")
    active = fields.Boolean("Active", default=True)

    @api.depends('student_ids')
    def _compute_no_of_students(self):
        for department in self:
            domain = [
                ('department_id', '=', department.id),
            ]

            department.no_of_students = self.env[
                'student.student'
            ].search_count(domain)

    def action_view_students(self):
        self.ensure_one()

        return {
            'type': 'ir.actions.act_window',
            'name': 'Students',
            'res_model': 'student.student',
            'view_mode': 'list,form',
            'domain': [
                ('department_id', '=', self.id),
            ],
        }

    def _compute_display_name(self):
        for department in self:
            if department.code:
                department.display_name = f"[{department.code}] {department.name}"
            else:
                department.display_name = department.name