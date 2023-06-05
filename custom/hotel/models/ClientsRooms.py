from odoo import api,models,fields
from odoo.exceptions import ValidationError
from datetime import datetime,date

class ClientsRooms(models.Model):
    _name = 'hotel.clients.rooms'
    _description = 'Clients rooms'
    _inherit = ['mail.thread','mail.activity.mixin']
    
    client = fields.Many2one(comodel_name = 'hotel.clients',required = True)
    room = fields.Many2one(comodel_name='hotel.rooms',required = True)
    date_in = fields.Datetime(required = True)
    date_out = fields.Datetime(required = True)
    status = fields.Selection([('booked','Booked'),('active','Active'),('done','Done')],required = True)
    
          
    @api.model
    def create(self, vals):
        
        self._check_room(vals)
        self._check_date_eq(vals)
        
        if vals.get('status') == 'active':
            self.env['hotel.clients.total'].create({'client':vals.get('client')})
        elif vals.get('status') == 'booked':
             date_in = datetime.strptime(vals.get('date_in'), '%Y-%m-%d %H:%M:%S')
             date_out = datetime.strptime(vals.get('date_out'), '%Y-%m-%d %H:%M:%S')
                
             now = datetime.now()
                
             if now > date_out:
                raise ValidationError('Issue with time')
        elif vals.get('status') == 'done':
            raise ValidationError('You cant set done when you creating record')
        client = super(ClientsRooms, self).create(vals)
        return client
    
    
    def write(self,vals):
        status = vals.get('status')
        if status == 'done':
            service = self.env['hotel.clients.services'].search([('client','=',self.client.id)])
            if service:
                service.write({'paid':True})
            total = self.env['hotel.clients.total'].search([('client','=',self.client.id)])
            total.write({'paid':True})
            n = datetime.now()
            datee = date(n.year,n.month,n.day)
            invoice = self.env['hotel.invoice'].search([('month','=',datee)])
            if not invoice:
                self.env['hotel.invoice'].create({'month':datee})
        elif status == 'active':
            self._check_date()
            service = self.env['hotel.clients.services'].search([('client','=',self.client.id)])
            total = self.env['hotel.clients.total'].search([('client','=',self.client.id)])
            if service:
                service.write({'paid':False})
            if not total:
                self.env['hotel.clients.total'].create({'client':self.client.id})
            else:
                total.write({'paid':False})
        elif status =='booked':
            service = self.env['hotel.clients.services'].search([('client','=',self.client.id)])
            total = self.env['hotel.clients.total'].search([('client','=',self.client.id)])
            service.unlink()
            total.unlink()
        return super(ClientsRooms, self).write(vals)

    def _check_room(self, vals):
        room_id = vals.get('room')
        date_in = vals.get('date_in')
        date_out = vals.get('date_out')
     
        
        conflicting_clients = self.search([
        ('room', '=', room_id),
        ('id', '!=', self.id),  # Exclude the current client if updating an existing record
        ('date_in', '<', date_out),
        ('date_out', '>', date_in),
        ('status','!=','done')
        ])

        if conflicting_clients:
            raise ValidationError('The room is not available on the specified dates')
    
    def _check_date_eq(self,vals):
        date_in = datetime.strptime(vals.get('date_in'), '%Y-%m-%d %H:%M:%S')
        date_out = datetime.strptime(vals.get('date_out'), '%Y-%m-%d %H:%M:%S')
        
        
        if date_in > date_out:
            raise ValidationError("Date in can't be greater than date out")
        
    def _check_date(self):
        date_in = self.date_in
        date_out = self.date_out
        
        now = datetime.now()
        
        if now > date_out:
            raise ValidationError('Issue with time')