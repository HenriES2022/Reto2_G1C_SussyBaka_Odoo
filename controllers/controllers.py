# -*- coding: utf-8 -*-
from odoo import http

# class SussyBaka(http.Controller):
#     @http.route('/sussy_baka/sussy_baka/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/sussy_baka/sussy_baka/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('sussy_baka.listing', {
#             'root': '/sussy_baka/sussy_baka',
#             'objects': http.request.env['sussy_baka.sussy_baka'].search([]),
#         })

#     @http.route('/sussy_baka/sussy_baka/objects/<model("sussy_baka.sussy_baka"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('sussy_baka.object', {
#             'object': obj
#         })