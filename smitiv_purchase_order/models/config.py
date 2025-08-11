from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    purchase_limit_amount = fields.Float(
        string="Purchase Approval Limit",
        config_parameter='purchase.approval_limit_amount',
        help="Purchase orders with total above this amount will require approval."
    )