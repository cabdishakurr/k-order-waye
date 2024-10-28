odoo.define('restaurant_orders.KitchenDisplay', function (require) {
    'use strict';

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');
    var QWeb = core.qweb;

    var KitchenDisplay = AbstractAction.extend({
        template: 'restaurant_orders.kitchen_display',
        
        init: function(parent, action) {
            this._super.apply(this, arguments);
            this.orderSound = new Audio('/restaurant_orders/static/src/sounds/new_order.mp3');
        },

        start: function() {
            this._super.apply(this, arguments);
            this._startPolling();
        },

        _startPolling: function() {
            this._pollOrders();
            setInterval(this._pollOrders.bind(this), 10000);
        },

        _pollOrders: function() {
            var self = this;
            this._rpc({
                model: 'restaurant.order',
                method: 'search_read',
                args: [[['state', 'in', ['to_cook', 'ready', 'completed']]]],
            }).then(function(orders) {
                self._updateDisplay(orders);
            });
        },

        _updateDisplay: function(orders) {
            // Play sound for new orders
            if (this._hasNewOrders(orders)) {
                this.orderSound.play();
            }
            
            // Update the display
            this.$('.order-list').empty();
            this._renderOrders(orders);
        },

        _hasNewOrders: function(orders) {
            // Compare with previous orders to detect new ones
            // Implementation depends on your specific requirements
            return false;
        }
    });

    core.action_registry.add('kitchen_display', KitchenDisplay);

    return KitchenDisplay;
});