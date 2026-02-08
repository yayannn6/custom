from odoo import models, fields, api

class InvoiceTaskLine(models.Model):
    _name = "invoice.task.line"
    _description = "Invoice Task Detail Line"

    move_id = fields.Many2one(
        "account.move",
        string="Invoice",
        ondelete="cascade",
        required=True
    )

    currency_id = fields.Many2one(
        "res.currency",
        related="move_id.currency_id",
        store=True,
        readonly=True
    )

    description = fields.Char(string="Description", required=True)
    quantity = fields.Float(string="Qty", default=1.0)

    price = fields.Monetary(
        string="Price",
        currency_field="currency_id"
    )

    uom = fields.Char(string="UoM")

    total = fields.Monetary(
        string="Total",
        currency_field="currency_id",
        compute="_compute_total",
        store=True
    )

    @api.depends("quantity", "price")
    def _compute_total(self):
        for line in self:
            line.total = line.quantity * line.price
