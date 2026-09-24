from odoo import api, fields, models


class SplitSaleWiz(models.TransientModel):
    _name = "split.sale.wiz"
    _description = "Split Sale Wiz"

    partner_id = fields.Many2one(
        "res.partner",
        string="Partner",
        required=True
    )

    def process_button(self):
        split_order_id = []

        sale_order = self.env["sale.order"].browse(
            self.env.context.get("active_id")
        )

        for line in sale_order.order_line:
            if line.split:
                split_order_id.append(line)

        new = self.env["sale.order"].create({
            "partner_id": self.partner_id.id
        })

        for element in split_order_id:
            element.write({
                "order_id": new.id
            })