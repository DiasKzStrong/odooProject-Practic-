from odoo import fields,models


class CategoryServices(models.Model):
    _name = 'hotel.category.services'
    _description = 'Category of services in hotel'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    
    name=fields.Char()