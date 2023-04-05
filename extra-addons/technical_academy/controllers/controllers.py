# -*- coding: utf-8 -*-
# from odoo import http


# class TechnicalTraining(http.Controller):
#     @http.route('/technical_training/technical_training/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/technical_training/technical_training/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('technical_training.listing', {
#             'root': '/technical_training/technical_training',
#             'objects': http.request.env['technical_training.technical_training'].search([]),
#         })

#     @http.route('/technical_training/technical_training/objects/<model("technical_training.technical_training"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('technical_training.object', {
#             'object': obj
#         })
