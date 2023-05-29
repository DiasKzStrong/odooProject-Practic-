from odoo import api,fields,models


class Clients(models.Model):
    _name = "hotel.clients"
    _description = "Model for clients"
    
    client_fio = fields.Char(string='FIO')
    passport_number = fields.Char(string='passpost number')
    telephone_number = fields.Char(string='telephone number')
    room = fields.Many2one(comodel_name='hotel.rooms')