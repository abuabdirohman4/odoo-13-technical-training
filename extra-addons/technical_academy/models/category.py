from odoo import models, fields

class Category(models.Model):
    _name = 'tech.course.category'
    _description = 'Data Kategori Kursus'

    name = fields.Char(string='Nama Kategori')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True)
    course_ids = fields.One2many(comodel_name='tech.course', inverse_name='category_id', string='Data Kursus')