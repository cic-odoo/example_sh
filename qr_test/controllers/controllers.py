# -*- coding: utf-8 -*-
# from odoo import http


# class QrTest(http.Controller):
#     @http.route('/qr_test/qr_test/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/qr_test/qr_test/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('qr_test.listing', {
#             'root': '/qr_test/qr_test',
#             'objects': http.request.env['qr_test.qr_test'].search([]),
#         })

#     @http.route('/qr_test/qr_test/objects/<model("qr_test.qr_test"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('qr_test.object', {
#             'object': obj
#         })
