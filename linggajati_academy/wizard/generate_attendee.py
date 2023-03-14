from odoo import api, fields, models


class SessionWizard(models.TransientModel):
    _name = 'session.wizard'
    _description = 'Popup untuk generate attendee'

    def _default_session(self):
        return self.env['linggajati.session'].browse(self._context.get('active_id'))

    session_id = fields.Many2one(
        comodel_name='linggajati.session', string='Sesi Kursus', required=True, default=_default_session)
    student_ids = fields.Many2many(
        comodel_name='res.partner', string='Siswa', domain="[('is_student', '=', True)]")

    def gen_attendee(self):
        #data_to_save = (0, 0, values)
        data_to_save = []
        if self.student_idx:
            data_to_save = []

