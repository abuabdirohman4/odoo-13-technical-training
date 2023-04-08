from odoo import models, fields

class Session(models.Model):
    _name = 'tech.session'
    _description = 'Sesi kurus yang berjalan'

    name = fields.Char(string='Nama')
    course_id = fields.Many2one(comodel_name='tech.course', string='Kursus')
    # instructor_id = fields.Many2one(comodel_name='res.partner', string='Pengajar')
    instructor_id = fields.Many2one(comodel_name='res.partner', string='Pengajar', domain="[('is_instructor', '=', True)]")
    session_date = fields.Date(string='Tanggal', default=fields.Date.today)
    min_attendee = fields.Integer(string='Minimal', default=0, required=True)
    description = fields.Text(string='Deskripsi')