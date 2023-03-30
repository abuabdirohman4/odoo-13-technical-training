# -*- coding: utf-8 -*-
# from odoo import http


# class LinggajatiTraining(http.Controller):
#     @http.route('/linggajati_training/linggajati_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/linggajati_training/linggajati_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('linggajati_training.listing', {
#             'root': '/linggajati_training/linggajati_training',
#             'objects': http.request.env['linggajati_training.linggajati_training'].search([]),
#         })

#     @http.route('/linggajati_training/linggajati_training/objects/<model("linggajati_training.linggajati_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('linggajati_training.object', {
#             'object': obj
#         })
