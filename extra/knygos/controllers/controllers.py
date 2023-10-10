# -*- coding: utf-8 -*-
from odoo import http

# class Knygos(http.Controller):
#     @http.route('/knygos/knygos/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/knygos/knygos/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('knygos.listing', {
#             'root': '/knygos/knygos',
#             'objects': http.request.env['knygos.knygos'].search([]),
#         })

#     @http.route('/knygos/knygos/objects/<model("knygos.knygos"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('knygos.object', {
#             'object': obj
#         })