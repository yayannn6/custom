from odoo import models, api


class ReportStatement(models.AbstractModel):
    _name = 'report.invoice_task_detail.statement_template'

    @api.model
    def _get_report_values(self, docids, data=None):
        wizard = self.env['statement.of.account.wizard'].browse(docids)
        partner = wizard.partner_id
        date_as_at = wizard.date_as_at

        account_types = []
        if wizard.account_type == 'receivable':
            account_types = ['asset_receivable']
            header_type = "Receivable"
        elif wizard.account_type == 'payable':
            account_types = ['liability_payable']
            header_type = "Payable"
        else:
            account_types = ['asset_receivable', 'liability_payable']
            header_type = "Outstanding"

        domain = [
            ('partner_id', '=', partner.id),
            ('move_id.state', '=', 'posted'),
            ('date', '<=', date_as_at),
            ('account_id.account_type', 'in', account_types),
            ('amount_residual', '!=', 0),
        ]

        lines = self.env['account.move.line'].search(domain, order="date asc")

        aging = {
            'total': 0.0,
            '1_30': 0.0,
            '31_60': 0.0,
            '61_90': 0.0,
            'over_90': 0.0,
        }

        for line in lines:
            residual = line.amount_residual
            aging['total'] += residual

            due_date = line.date_maturity or line.date
            delta = (date_as_at - due_date).days

            if delta <= 30:
                aging['1_30'] += residual
            elif delta <= 60:
                aging['31_60'] += residual
            elif delta <= 90:
                aging['61_90'] += residual
            else:
                aging['over_90'] += residual

        return {
            'wizard': wizard,
            'partner': partner,
            'lines': lines,
            'aging': aging,
            'header_type': header_type,
        }