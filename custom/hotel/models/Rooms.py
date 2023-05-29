from odoo import api,fields,models


class Room(models.Model):
    _name = 'hotel.rooms'
    _description = 'Model for rooms in hotel'
    
    number = fields.Integer()
    category = fields.Many2one(comodel_name='hotel.roomcategory')