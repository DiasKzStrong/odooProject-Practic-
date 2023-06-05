from odoo import api,fields,models


class Room(models.Model):
    _name = 'hotel.rooms'
    _description = 'Model for rooms in hotel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    number = fields.Integer()
    category = fields.Many2one(comodel_name='hotel.roomcategory')
    price_for_day = fields.Monetary('Price',currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', 'Currency')
    
    def name_get(self):
        return [(self.id,f'Number {res.number}') for res in self]