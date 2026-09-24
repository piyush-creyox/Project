from odoo import  fields, models


class DepartmentConf(models.TransientModel):
    _name = "department.conf"
    _description = "Department.conf"

    type = fields.Selection([('create', 'Create'), ('write', 'Write')],required=True)
    name = fields.Char(string="Name")
    code = fields.Char(string="Code")
    department_id = fields.Many2one("department.department")

    def process_method_create(self):
        values = {'name': self.name, 'code': self.code, 'active': True}
        self.env['department.department'].create(values)

    def process_method_write(self):
        if self.name:
            self.department_id.write({
                'name': self.name,
                'code': self.code,})
