# -*- coding: utf-8 -*-
# from odoo import http


# class MyProjectExtension(http.Controller):
#     @http.route('/my_project_extension/my_project_extension', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/my_project_extension/my_project_extension/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('my_project_extension.listing', {
#             'root': '/my_project_extension/my_project_extension',
#             'objects': http.request.env['my_project_extension.my_project_extension'].search([]),
#         })

#     @http.route('/my_project_extension/my_project_extension/objects/<model("my_project_extension.my_project_extension"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('my_project_extension.object', {
#             'object': obj
#         })
