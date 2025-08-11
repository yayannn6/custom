# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    approval_state = fields.Selection([
        ('draft', 'Draft'),
        ('to_approve', 'To Approve'),
        ('approved', 'Approved')
    ], string="Approval Status", default="draft", tracking=True)

    LIMIT_AMOUNT = 1000 

    def button_confirm(self):
        for order in self:
            if order.amount_total >= self.LIMIT_AMOUNT and order.approval_state != 'approved':
                order.approval_state = 'to_approve'
                raise UserError(_("This order exceeds the {:,.0f} limit and must be approved first.").format(self.LIMIT_AMOUNT))
        return super().button_confirm()

    def action_approve_order(self):
        """Tombol approve, hanya Purchase Manager yang bisa"""
        if not self.env.user.has_group('purchase.group_purchase_manager'):
            raise UserError(_("You do not have the right to approve this order."))
        for order in self:
            order.approval_state = 'approved'
        return True
