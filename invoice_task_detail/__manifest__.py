{
    "name": "Invoice Task Detail",
    "version": "1.0",
    "category": "Accounting",
    'author': "Yayan Hidayatulloh",
    'website': "",
    "summary": "Custom task detail & GST on invoice",
    "depends": ["account"],
    "data": [
        "views/account_move_view.xml",
        "security/ir.model.access.csv",
        "report/report_tax_invoice.xml",
        "report/report.xml",
    ],
    "installable": True,
}
