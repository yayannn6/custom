from odoo import models, fields

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    our_ref = fields.Char(string="Our Ref")
    attn = fields.Char(string="Attention")
    re_subject = fields.Char(string="Reference (RE)")
    delivery_terms = fields.Char(string="Delivery Terms")
    validity_terms = fields.Char(string="Validity Terms")
    payment_terms_note = fields.Char(string="Payment Terms Note")
