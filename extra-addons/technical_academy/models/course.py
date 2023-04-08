from odoo import models, fields

class Course(models.Model):
    _name = 'tech.course'
    _description = 'Data Kursus'

    name = fields.Char(string='Nama Kursus')
    description = fields.Text(string='Deskripsi')
    active = fields.Boolean(string='Active', default=True)
    category_id = fields.Many2one(comodel_name='tech.course.category', string='Kategori')
