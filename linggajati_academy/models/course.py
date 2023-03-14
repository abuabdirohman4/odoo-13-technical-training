from odoo import api, fields, models


class Course(models.Model):
    _name = 'linggajati.course'
    _description = 'Data Kursus'

    # ofm2
    name = fields.Char(string='Nama Kursus')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True,)
    category_id = fields.Many2one(
        comodel_name='linggajati.training.category', string='Kategori')
