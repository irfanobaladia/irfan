# -*- coding: utf-8 -*-
# from odoo import http


# class /opt/odoo13/odoo-custom-addons/rkiza(http.Controller):
#     @http.route('//opt/odoo13/odoo-custom-addons/rkiza//opt/odoo13/odoo-custom-addons/rkiza/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('//opt/odoo13/odoo-custom-addons/rkiza//opt/odoo13/odoo-custom-addons/rkiza/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('/opt/odoo13/odoo-custom-addons/rkiza.listing', {
#             'root': '//opt/odoo13/odoo-custom-addons/rkiza//opt/odoo13/odoo-custom-addons/rkiza',
#             'objects': http.request.env['/opt/odoo13/odoo-custom-addons/rkiza./opt/odoo13/odoo-custom-addons/rkiza'].search([]),
#         })

#     @http.route('//opt/odoo13/odoo-custom-addons/rkiza//opt/odoo13/odoo-custom-addons/rkiza/objects/<model("/opt/odoo13/odoo-custom-addons/rkiza./opt/odoo13/odoo-custom-addons/rkiza"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('/opt/odoo13/odoo-custom-addons/rkiza.object', {
#             'object': obj
#         })
