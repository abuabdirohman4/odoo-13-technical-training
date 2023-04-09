from odoo import models, fields

class SessionWIzard(models.TransientModel):
    _name = 'session.wizard'
    _description = 'Popup untuk generate attendee'

    def _default_session(self):
        return self.env['tech.session'].browse(self._context.get('active_id'))
    
    session_id = fields.Many2one(comodel_name='tech.session', string='Sesi Kursus', required=True, default=_default_session)
    student_ids = fields.Many2many(comodel_name='res.partner', string='Siswa', domain="[('is_student', '=', True)]")

    def gen_attendee(self):
        # Debugging
        # import ipdb
        # ipdb.set_trace()

        data_to_save = []
        if self.student_ids:
            # Pythonic (Cara Mentor)
            # data_to_save = [(0, 0, {'name': '1234', 'student_id': x.id,}) for x in self.student_ids]
            for student in self.student_ids:
                data_to_save.append((0, 0,{'name': '1234', 'student_id': student.id}))

        if data_to_save:
            self.session_id.attendee_ids = data_to_save
        
        return {}