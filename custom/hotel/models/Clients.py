from odoo import api,fields,models
from odoo.exceptions import ValidationError


class Clients(models.Model):
    _name = "hotel.clients"
    _description = "Model for clients"
    _inherit = ['mail.thread', 'mail.activity.mixin']
            
    client_fio = fields.Char(string='FIO',required = True)
    passport_number = fields.Char(string='passpost number',required = True)
    telephone_number = fields.Char(string='telephone number',required = True)
    sex = fields.Selection([('male','Male'),('female','Female')],required = True)
    client_services = fields.One2many(comodel_name = 'hotel.clients.services',inverse_name = 'client')
    client_rooms = fields.One2many(comodel_name = 'hotel.clients.rooms',inverse_name = 'client')
    client_total = fields.One2many(comodel_name = 'hotel.clients.total',inverse_name = 'client')
    
   
       
    def name_get(self):
        return [(res.id,res.client_fio) for res in self]