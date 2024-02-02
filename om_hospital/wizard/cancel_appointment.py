import datetime
from odoo import api, fields, models, _
from odoo.exceptions import ValidationError


class CancelAppointmentWizard(models.TransientModel):
    _name = "cancel.appointment.wizard"
    _description = "Cancel Appointment Wizard"

    @api.model
    def default_get(self, fields):
        res = super(CancelAppointmentWizard, self).default_get(fields)
        res['date_cancel'] = datetime.date.today()
        if self.env.context.get('active_id'):
            res['appointment_id'] = self.env.context.get('active_id')
        return res

    appointment_id = fields.Many2one('hospital.appointment', string="Appointment", domain=[('state', '=', 'draft'), ('priority', 'in', ('0', '1', False))])
    reason = fields.Text(string="Reason", default='Test Reason')
    date_cancel = fields.Date(string="Cancellation Date")

    def action_cancel(self):
        if self.appointment_id.booking_date == fields.Date.today():
            raise ValidationError(_("Sorry, cancellation is not allowed on the same day of booking"))
        self.appointment_id.state = 'cancel'
        return