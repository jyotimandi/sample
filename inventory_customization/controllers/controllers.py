# -*- coding: utf-8 -*-
# from odoo import http


# class InvenrtoryCustomization(http.Controller):
#     @http.route('/inventory_customization/inventory_customization/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/inventory_customization/inventory_customization/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('inventory_customization.listing', {
#             'root': '/inventory_customization/inventory_customization',
#             'objects': http.request.env['inventory_customization.inventory_customization'].search([]),
#         })

#     @http.route('/inventory_customization/inventory_customization/objects/<model("inventory_customization.inventory_customization"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('inventory_customization.object', {
#             'object': obj
#         })
