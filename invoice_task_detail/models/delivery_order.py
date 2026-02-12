from odoo import models, fields

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    attn = fields.Char(string="Attention")
    do_no = fields.Char(string="DO Number")
    po_no = fields.Char(string="PO Number")
