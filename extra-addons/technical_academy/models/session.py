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
    attendee_ids = fields.One2many(comodel_name='tech.session.attendee', inverse_name='session_id', string='Data Peserta')
    state = fields.Selection(string='State', selection=[
        ('draft', 'Draft'), 
        ('done', 'Done'),
        ('cancel', 'Cancel'),
    ], default='draft', required=True, readonly=True)

class SessionAttendee(models.Model):
    _name = 'tech.session.attendee'
    _description = 'Peserta di sesi kursus'

    name = fields.Char(string='No Pendaftaran', required=True)
    student_id = fields.Many2one(comodel_name='res.partner', string='Siswa', domain="[('is_student', '=', True)]", required=True)
    description = fields.Text(string='Deskripsi')
    session_id = fields.Many2one(comodel_name='tech.session', string='Sesi Kursus')