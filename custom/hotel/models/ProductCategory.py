from odoo import api,fields,models


class ProductCategory(models.Model):
    _name = 'hotel.products.category'
    
    
    name = fields.Char()