# -*- coding: utf-8 -*-
# from odoo import http


# class /mnt/extra-addons/smitivPurchaseOrder(http.Controller):
#     @http.route('//mnt/extra-addons/smitiv_purchase_order//mnt/extra-addons/smitiv_purchase_order', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//mnt/extra-addons/smitiv_purchase_order//mnt/extra-addons/smitiv_purchase_order/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('/mnt/extra-addons/smitiv_purchase_order.listing', {
#             'root': '//mnt/extra-addons/smitiv_purchase_order//mnt/extra-addons/smitiv_purchase_order',
#             'objects': http.request.env['/mnt/extra-addons/smitiv_purchase_order./mnt/extra-addons/smitiv_purchase_order'].search([]),
#         })

#     @http.route('//mnt/extra-addons/smitiv_purchase_order//mnt/extra-addons/smitiv_purchase_order/objects/<model("/mnt/extra-addons/smitiv_purchase_order./mnt/extra-addons/smitiv_purchase_order"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/mnt/extra-addons/smitiv_purchase_order.object', {
#             'object': obj
#         })
