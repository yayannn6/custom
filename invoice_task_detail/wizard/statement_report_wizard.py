from odoo import models, fields, api
from datetime import date


class StatementWizard(models.TransientModel):
    _name = 'statement.of.account.wizard'
    _description = 'Statement of Account Wizard'

    partner_id = fields.Many2one('res.partner', required=True)
    date_as_at = fields.Date(default=fields.Date.today, required=True)

    account_type = fields.Selection([
        ('receivable', 'Receivable'),
        ('payable', 'Payable'),
        ('both', 'Both'),
    ], default='receivable', required=True)

    def action_print(self):
        return self.env.ref(
            'invoice_task_detail.statement_of_account_report'
        ).report_action(self)