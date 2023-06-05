from odoo import api, fields, models
from datetime import datetime
from dateutil.relativedelta import relativedelta

class MonthlyInvoice(models.Model):
    _name = 'hotel.invoice'
    _description = 'Monthly Invoice'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    
    total_price = fields.Monetary('Total Price', compute='_compute_total_price', currency_field='currency_id')
    month = fields.Date(string='Month', store=True, readonly=True)
    currency_id = fields.Many2one('res.currency', 'Currency')
    
    @api.depends('month')
    def _compute_total_price(self):
        for record in self:
            
            print(record.month.month)
            
            last_month = record.month
            last_month_start = last_month.replace(day=1)
            last_month_end = last_month_start + relativedelta(day=31)
            
            print('end',last_month_end)
            print('start',last_month_start)
            
            total_prices = self.env['hotel.clients.total'].search([
                ('paid', '=', True),
                ('write_date', '>=', last_month_start),
                ('write_date', '<=', last_month_end)
            ])
            
            print('total',total_prices)
            
            total_price = sum(total.total_price for total in total_prices)
            record.total_price = total_price