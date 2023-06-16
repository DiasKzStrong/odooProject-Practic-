from odoo import fields,models,api
from odoo.exceptions import ValidationError




class Products(models.Model):
    _name = 'hotel.products'
    
    
    category = fields.Many2one(comodel_name = 'hotel.products.category')
    product_name = fields.Char()
    product_price = fields.Monetary('Product Price',currency_field='currency_id')
    currency_id = fields.Many2one('res.currency', 'Currency')
    
    