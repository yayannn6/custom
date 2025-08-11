# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved')
    ], string="Approval Status", default="draft")

    LIMIT_AMOUNT = 1000 

    @api.onchange('amount_total')
    def _compute_approval_state(self):
        limit = float(self.env['ir.config_parameter'].sudo().get_param('purchase.approval_limit_amount', default=0))
        for order in self:
            if order.amount_total >= limit and order.approval_state != 'approved':
                order.approval_state = 'to_approve'


    def button_confirm(self):
        limit = float(self.env['ir.config_parameter'].sudo().get_param('purchase.approval_limit_amount', default=0))
        for order in self:
            if order.amount_total >= limit and order.approval_state != 'approved':
                order.write({'approval_state': 'to_approve'})
                raise UserError(_("This order exceeds the {:,.0f} limit and must be approved first.").format(limit))
        return super().button_confirm()

    def action_approve_order(self):
        """Tombol approve, hanya Purchase Manager yang bisa"""
        if not self.env.user.has_group('purchase.group_purchase_manager'):
            raise UserError(_("You do not have the right to approve this order."))
        for order in self:
            order.approval_state = 'approved'
        return True
