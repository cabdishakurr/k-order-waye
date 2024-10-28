from odoo import models, fields, api
from datetime import datetime

class RestaurantOrder(models.Model):
    _name = 'restaurant.order'
    _description = 'Restaurant Order'
    _order = 'create_date desc'

    name = fields.Char('Order Reference', required=True, copy=False, readonly=True, default='New')
    table_number = fields.Char('Table Number', required=True)
    customer_name = fields.Char('Customer Name')
    state = fields.Selection([
        ('to_cook', 'To Cook'),
        ('ready', 'Ready'),
        ('completed', 'Completed')
    ], string='Status', default='to_cook', tracking=True)
    order_items = fields.One2many('restaurant.order.line', 'order_id', string='Order Items')
    preparation_time = fields.Float('Preparation Time (minutes)')
    create_date = fields.Datetime('Order Time', default=fields.Datetime.now)

    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('restaurant.order') or 'New'
        return super(RestaurantOrder, self).create(vals)

class RestaurantOrderLine(models.Model):
    _name = 'restaurant.order.line'
    _description = 'Restaurant Order Line'

    order_id = fields.Many2one('restaurant.order', string='Order Reference')
    product_id = fields.Many2one('product.product', string='Product', required=True)
    quantity = fields.Integer('Quantity', default=1)
    notes = fields.Text('Special Instructions')