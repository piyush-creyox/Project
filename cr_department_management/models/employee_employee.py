from odoo import models, fields, api
from odoo.odoo.api import onchange, depends


class Department(models.Model):
    _name = "employee.employee"
    _description = "employee.employee"
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char("Name", required = True)
    image = fields.Binary("Image")
    street = fields.Char("Street")
    city = fields.Char("City")
    zip = fields.Char("Zip")
    state_id = fields.Many2one('res.country.state', string='State')
    country_id = fields.Many2one('res.country', string='Country')
    birthdate = fields.Date("Birthdate")
    age = fields.Float("Age",compute='_compute_age',store=True,help='Age is automatically calculated from the birthdate.')
    mobile = fields.Char("Mobile",help='Enter the student mobile number.')
    email = fields.Char("Email")
    barcode = fields.Char("Barcode")
    job_time = fields.Selection([('Full_time', 'Full_time'),('Part_time', 'Part_time'),],string='Job_time')
    notes = fields.Html("Notes")
    remarks = fields.Text("Remarks")
    is_hod = fields.Boolean("Is_HOD")
    active = fields.Boolean("Active",default = True)

    @api.onchange('mobile')
    def _onchange_mobile(self):
        self.barcode = self.mobile


    @api.depends('birthdate')
    def _compute_age(self):
        for employee in self:
            if employee.birthdate:
                today = fields.Date.today()
                employee.age = today.year - employee.birthdate.year

                if (today.month, today.day) < (
                        employee.birthdate.month,
                        employee.birthdate.day
                ):
                    employee.age -= 1
            else:
                employee.age = 0

