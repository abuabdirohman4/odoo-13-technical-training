from odoo import api, fields, models, _
from odoo.exceptions import AccessError, UserError


class Session(models.Model):
    _name = 'linggajati.session'
    _description = 'Sesi Kursus Yang Berjalan'

    name = fields.Char(string='Nama Sesi')
    course_id = fields.Many2one(
        comodel_name='linggajati.course', string='Kursus')
    instructor_id = fields.Many2one(
        comodel_name='res.partner', string='Pengajar', domain="[('is_instructor', '=', True)]")
    session_date = fields.Date(string='Tanggal', default=fields.Date.today,)
    min_attendee = fields.Integer(string='Minimal', default=0, required=True,)
    description = fields.Text(string='Deskripsi')
    attendee_ids = fields.One2many(
        comodel_name='linggajati.session.attendee', inverse_name='session_id', string='Data Peserta')
    state = fields.Selection(string='State', selection=[
        ('draft', 'Draft'),
        ('done', 'Done'),
        ('cancel', 'Cancel')
    ], default='draft', required=True, readonly=True,)

    taken_seats = fields.Float(
        string='Jumlah Peserta Terdaftar', compute='_compute_taken_seats', store=True,)
    email = fields.Char(string='Email Pengajar',
                        related="instructor_id.email", store=True,)

    @api.onchange('min_attendee')
    def _onchange_min_attendee(self):
        if self.min_attendee < 0:
            return {
                'warning': {
                    'title': "Tidak Valud!!!",
                    'message': "minimal peserta tidak boleh minus",
                },
            }

    @api.depends('min_attendee', 'attendee_ids')
    def _compute_taken_seats(self):
        for record in self:
            if not record.min_attendee:
                record.taken_seats = 0.0
            else:
                record.taken_seats = 100.0 * (len(record.attendee_ids) / record.min_attendee)

    def action_done(self):
        # validasi jika ada
        self.write({'state': 'done'})
    # write itu mksudnya update

    def action_cancel(self):
        self.write({'state': 'cancel'})

    def action_draft(self):
        self.write({'state': 'draft'})

    def unlink(self):
        for record in self:
            if record.state != 'draft':
                raise UserError(
                    _('Maaf data selain draft tidak boleh dihapus.'))
        return super(Session, self).unlink()


class SessionAttendee(models.Model):
    _name = 'linggajati.session.attendee'
    _description = 'Peserta di sesi kursus'

    name = fields.Char(string='No Pendaftaran', required=True,)
    student_id = fields.Many2one(comodel_name='res.partner', string='Siswa',
                                 domain="[('is_student', '=', True)]", required=True,)
    description = fields.Text(string='description')
    session_id = fields.Many2one(
        comodel_name='linggajati.session', string='Sesi Kursus')
