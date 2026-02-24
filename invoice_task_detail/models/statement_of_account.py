from odoo import models, api, fields
from datetime import datetime


class ReportStatementOfAccount(models.AbstractModel):
    _name = 'report.statement_of_account.statement_template'
    _description = 'Statement of Account Report'

    @api.model
    def _get_report_values(self, docids, data=None):
        partner = self.env['res.partner'].browse(docids)

        date_today = fields.Date.today()

        # =========================
        # PARTNER LEDGER
        # =========================
        ledger_lines = self.env['account.move.line'].search([
            ('partner_id', '=', partner.id),
            ('parent_state', '=', 'posted'),
            ('account_id.account_type', '=', 'asset_receivable')
        ], order='date asc')

        # =========================
        # AGING
        # =========================
        aging_data = {
            '0_30': 0.0,
            '31_60': 0.0,
            '61_90': 0.0,
            'over_90': 0.0,
        }

        for line in ledger_lines:
            if line.date_maturity:
                delta = (date_today - line.date_maturity).days
                balance = line.debit - line.credit

                if delta <= 30:
                    aging_data['0_30'] += balance
                elif delta <= 60:
                    aging_data['31_60'] += balance
                elif delta <= 90:
                    aging_data['61_90'] += balance
                else:
                    aging_data['over_90'] += balance

        return {
            'doc_ids': docids,
            'doc_model': 'res.partner',
            'docs': partner,
            'ledger_lines': ledger_lines,
            'aging': aging_data,
            'today': date_today,
        }