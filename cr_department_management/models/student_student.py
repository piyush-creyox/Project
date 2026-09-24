from re import search

from odoo import models, fields, api
from odoo.odoo.api import onchange, depends


class Department(models.Model):
    _name = "student.student"
    _description = "student.student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = "city"


    name = fields.Char("Name", required=True)
    image = fields.Binary("Image")
    street = fields.Char("Street")
    city = fields.Char("City")
    zip = fields.Char("Zip")
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    birthdate = fields.Date("Birthdate")
    age = fields.Float("Age", compute='_compute_age', store=True,
                       help='Age is automatically calculated from the birthdate.')
    mobile = fields.Char("Mobile", help='Enter the student mobile number.')
    email = fields.Char("Email")
    barcode = fields.Char("Barcode")
    department_id = fields.Many2one('department.department', string='Department',
                                    default=lambda self: self.env['department.department'].search([], limit=1))
    type = fields.Selection([('external', 'External'), ('internal', 'Internal'), ], string='Type')
    notes = fields.Html("Notes")
    remarks = fields.Text("Remarks")
    is_cr = fields.Boolean("Is_cr", help='Check this field if the student is a Class Representative.')
    cr_start_date = fields.Date("Cr_Start_Date")
    cr_end_date = fields.Date("Cr_End_Date")
    no_of_votes = fields.Integer("No_Of_Votes")
    active = fields.Boolean("Active", default=True)
    dept_code = fields.Char(string='Department Code', related='department_id.code', store=True)

    # onchange
    @api.onchange('mobile')
    def _onchange_mobile(self):
        self.barcode = self.mobile

    # compute
    @api.depends('birthdate')
    def _compute_age(self):
        for student in self:
            if student.birthdate:
                today = fields.Date.today()
                student.age = today.year - student.birthdate.year
                if (today.month, today.day) < (
                        student.birthdate.month,
                        student.birthdate.day
                ):
                    student.age -= 1
            else:
                student.age = 0

    # ir_corn
    def check_students(self):
        students = self.search([])
        for student in students:
            if student.remarks == "Checked by Cron":
                pass
            else:
                student.remarks = "Checked by Cron"

    # write method
    def action_write_student(self):
        self.write({
            "name": "Pi",
            "mobile": "99123456789",
        })

    # search method
    def action_search_student(self):
        students = self.search([
            ("name", "=", "Piyush")
        ])
        return {
            "type": "ir.actions.act_window",
            "name": "Students",
            "res_model": "student.student",
            "view_mode": "list,form",
            "domain": [("name", "=", "Piyush")],
            "target": "current",
        }

    # unlink method
    def action_unlink_student(self):
        self.unlink()

    # browse method
    def action_browse_student(self):
        self.browse()
        return {
            "type": "ir.actions.act_window",
            "name": "Students",
            "res_model": "student.student",
            "view_mode": "list,form",
            "target": "current",
            "limit": "5",
        }

    # read method
    def action_read_student(self):
        students = self.env['student.student'].search([], limit=4)
        res = students.read([
            'name',
            'age',
            'email'
        ])
        print(res)
        return res

    # name_search method

    # create override
    @api.model
    def create(self, vals):
        if vals.get("mobile"):
            vals["barcode"] = vals["mobile"]
        print("before ", vals)

        student = super().create(vals)
        print("after ", student)

        return student

    # Write override
    @api.model
    def write(self, vals):
        print(vals)
        res = super().write(vals)
        print(res)
        return res

    # Search override

    @api.model
    def search(self, domain, offset=0, limit=None, order=None):
        print("domain", domain)
        record = super().search(
            domain,
            offset=offset,
            limit=limit,
            order=order
        )
        print("Record", record)
        return record

    # Unlink override
    def unlink(self):
        for student in self:
            print("Deleting student:", student.name)

        return super().unlink()

# Browse override
