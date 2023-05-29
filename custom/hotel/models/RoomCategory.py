from odoo import api,models,fields

class RoomCategory(models.Model):
    _name = 'hotel.roomcategory'
    _description = 'Category of rooms in hotel'
    
    name = fields.Char(string='Name')
    
    def __str__(self):
        return f'{self.name}'
    
