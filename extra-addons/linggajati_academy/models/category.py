from odoo import api, fields, models

class Category(models.Model):
    _name = 'linggajati.training.category'
    _description = 'Data Kategori Pelatihan'

    name = fields.Char(string='Nama Kategori')
    description = fields.Text(string='Kategori')
    active = fields.Boolean(string='Active', default=True,)
    course_ids = fields.One2many(comodel_name='linggajati.course', inverse_name='category_id', string='Data Kursus')
    
