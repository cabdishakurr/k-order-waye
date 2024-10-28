from odoo import http
from odoo.http import request

class KitchenDisplay(http.Controller):
    @http.route('/restaurant/kitchen_display', type='json', auth='user')
    def get_orders(self):
        orders = request.env['restaurant.order'].search_read(
            [('state', 'in', ['to_cook', 'ready', 'completed'])],
            ['name', 'table_number', 'customer_name', 'state', 'order_items', 'preparation_time', 'create_date']
        )
        return orders