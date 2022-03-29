# -*- coding: utf-8 -*-
# from odoo import http


# class Karyawan(http.Controller):
#     @http.route('/karyawan/karyawan/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/karyawan/karyawan/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('karyawan.listing', {
#             'root': '/karyawan/karyawan',
#             'objects': http.request.env['karyawan.karyawan'].search([]),
#         })

#     @http.route('/karyawan/karyawan/objects/<model("karyawan.karyawan"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('karyawan.object', {
#             'object': obj
#         })
