from odoo import models, fields, api

class Purchase(models.Model):
    _inherit = "purchase.order"

    requested_by = fields.Many2one("res.users", "Requested By")
    date_required = fields.Date("Date Required")
    project = fields.Many2one("project.project", "Project")
    delivery_address = fields.Text("Delivery Address")
    attn = fields.Char(string="Attn")

class PurchaseLine(models.Model):
    _inherit = "purchase.order.line"

    remark = fields.Char("Remark")
