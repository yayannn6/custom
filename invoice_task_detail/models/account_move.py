from odoo import models, fields, api

class AccountMove(models.Model):
    _inherit = "account.move"

    attn = fields.Char(string="Attn")

    task_line_ids = fields.One2many(
        "invoice.task.line",
        "move_id",
        string="Task Details"
    )


    amount_before_tax_manual = fields.Monetary(
        string="Total Before Tax",
        currency_field="currency_id"
    )

    gst_amount = fields.Monetary(
        string="GST 9%",
        currency_field="currency_id",
        compute="_compute_gst",
        store=True
    )

    grand_total = fields.Monetary(
        string="Grand Total",
        currency_field="currency_id",
        compute="_compute_gst",
        store=True
    )

    @api.depends("amount_before_tax_manual")
    def _compute_gst(self):
        for move in self:
            move.gst_amount = move.amount_before_tax_manual * 0.09
            move.grand_total = move.amount_before_tax_manual + move.gst_amount
