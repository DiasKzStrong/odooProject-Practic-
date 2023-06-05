from odoo import api,fields,models
from odoo.exceptions import ValidationError
import datetime

class ClientServices(models.Model):
    _name = 'hotel.clients.services'
    _description = 'Services that used by client'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _d = datetime.timedelta(0)
    
    client = fields.Many2one(comodel_name = 'hotel.clients')
    service = fields.Many2one(comodel_name = 'hotel.services')
    date = fields.Datetime(default=lambda self: datetime.datetime.now())
    quantity = fields.Integer(default = 1)
    paid = fields.Boolean(default=True)
    
    @api.model
    def create(self,vals):
        
        if vals.get('quantity') < 0:
            raise ValidationError("quantity can't be lower than 0")
        self._check_date(vals)
        self._check_is_active(vals)
      
        return super(ClientServices,self).create(vals)

    def write(self,vals):
        raise ValidationError('Changing is not accessible')

    def _check_date(self,vals):
        client = self.env['hotel.clients.rooms'].search([('client','=',vals.get('client'))])
        d = vals.get('date')
        date = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S') 
        date1 = client.date_in - date
        date2 = date - client.date_out
        if date1 > self._d or date2 > self._d:
            raise ValidationError('Date is not proper for this client')

    def _check_is_active(self,vals):
        client = self.env['hotel.clients.rooms'].search([('client','=',vals.get('client'))])
        if client.status != 'active':
            raise ValidationError('This client is not active')