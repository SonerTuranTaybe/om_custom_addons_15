# -*- coding: utf-8 -*-

from odoo import api, fields, models
from datetime import date



class HospitalPatient(models.Model):
    _name = "hospital.patient"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Hospital Patient"

    # Kayıt adını belirtir girilmez ise default name degiskenini alır
    # _rec_name = "name"
    name = fields.Char(string='Name', tracking=True)
    date_of_birth = fields.Date(string="Date of Birth")
    # bu model değerini bir fonksiyondan alacak
    calculated_age = fields.Integer(string='Calculated Age', compute="_compute_calculated_age")
    ref = fields.Char(string='Reference')
    age = fields.Integer(string='Age', tracking=True)
    gender = fields.Selection([('male', 'Male'), ('female', 'Female')], string="Gender")
    active = fields.Boolean(string="Active", default=True)
    appointment_id = fields.Many2one('hospital.appointment', string="Appointment")
    image = fields.Image(string="Image")
    tag_ids = fields.Many2many('patient.tag', string="Tags")

    # compute kullanımı model de bulunan field için değer sağlanması (@decarator= anlık değşim gözlenmesi için)
    @api.depends('date_of_birth')
    def _compute_calculated_age(self):
        for rec in self:
            today = date.today()
            if rec.date_of_birth:
                rec.calculated_age = today.year - rec.date_of_birth.year
            else:
                rec.calculated_age = 1
