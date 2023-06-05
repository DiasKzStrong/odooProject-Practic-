from odoo import api,fields,models
from datetime import datetime

class TotalPrice(models.Model):
    _name = 'hotel.clients.total'
    _description = 'Total price for client'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    client = fields.Many2one(comodel_name = 'hotel.clients')
    total_price = fields.Monetary('Total Price',compute='_compute_total_price',currency_field='currency_id')
    paid = fields.Boolean(default=False)
    currency_id = fields.Many2one('res.currency', 'Currency')
    
    @api.depends('client')
    def _compute_total_price(self):
         for record in self:
            services = self.env['hotel.clients.services'].search([('client', '=', record.client.id)])
            total_price = sum(service.quantity * service.service.price for service in services)
            total_price += self.calc_price_room(record)
            record.total_price = total_price
    
    def calc_price_room(self,record):
        room = self.env['hotel.clients.rooms'].search([('client','=',record.client.id)])
        date_in = room.date_in
        date_out = room.date_out
        if date_in and date_out:
            d = date_out - date_in
            total = d.days*room.room.price_for_day
            return total
        return 0 
            
    