{
    'name': 'Restaurant Orders',
    'version': '1.0',
    'category': 'Sales',
    'summary': 'Restaurant Order Management with Kitchen Display',
    'description': """
        Restaurant Order Management System with:
        - Kitchen Display Interface
        - Real-time Order Updates
        - Sound Notifications
        - Order Status Tracking
    """,
    'depends': ['base', 'web', 'point_of_sale'],
    'data': [
        'security/ir.model.access.csv',
        'views/restaurant_order_views.xml',
        'views/kitchen_display_views.xml',
        'views/menu_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'restaurant_orders/static/src/js/kitchen_display.js',
            'restaurant_orders/static/src/css/kitchen_display.css',
            'restaurant_orders/static/src/sounds/new_order.mp3',
        ],
    },
    'application': True,
    'installable': True,
}