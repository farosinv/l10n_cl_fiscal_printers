# -*- coding: utf-8 -*-
from openerp import http

# class L10nClFiscalPrinters(http.Controller):
#     @http.route('/l10n_cl_fiscal_printers/l10n_cl_fiscal_printers/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/l10n_cl_fiscal_printers/l10n_cl_fiscal_printers/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('l10n_cl_fiscal_printers.listing', {
#             'root': '/l10n_cl_fiscal_printers/l10n_cl_fiscal_printers',
#             'objects': http.request.env['l10n_cl_fiscal_printers.l10n_cl_fiscal_printers'].search([]),
#         })

#     @http.route('/l10n_cl_fiscal_printers/l10n_cl_fiscal_printers/objects/<model("l10n_cl_fiscal_printers.l10n_cl_fiscal_printers"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('l10n_cl_fiscal_printers.object', {
#             'object': obj
#         })