from odoo import fields,models


class Services(models.Model):
    _name = 'hotel.services'
    _description = 'Services in hotel'
    
    services_category = fields.Many2one(comodel_name='hotel.category.services')
    name = fields.Char()
    price = fields.Monetary('Price',currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', 'Currency')