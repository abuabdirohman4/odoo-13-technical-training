from odoo import models, fields

class SessionWIzard(models.TransientModel):
    _name = 'session.wizard'
    _description = 'Popup untuk generate attendee'

    session_id = fields.Many2one(comodel_name='tech.session', string='Sesi Kursus', required=True)
    student_ids = fields.Many2many(comodel_name='res.partner', string='Siswa')