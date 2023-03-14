from odoo import api, fields, models


class Sales(models.Model):
    _inherit = 'sale.order'

    no_kontrak = fields.Char(string='No. Kontrak')
