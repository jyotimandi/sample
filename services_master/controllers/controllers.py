# -*- coding: utf-8 -*-
# from odoo import http


# class ServicesMaster(http.Controller):
#     @http.route('/services_master/services_master/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/services_master/services_master/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('services_master.listing', {
#             'root': '/services_master/services_master',
#             'objects': http.request.env['services_master.services_master'].search([]),
#         })

#     @http.route('/services_master/services_master/objects/<model("services_master.services_master"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('services_master.object', {
#             'object': obj
#         })
