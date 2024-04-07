odoo.define('my_project_extension.dashboard', function (require) {
    'use strict';

    var AbstractAction = require('web.AbstractAction');
    var core = require('web.core');

    var Dashboard = AbstractAction.extend({
        template: 'DashboardDashboard',

        init: function (parent, context) {
            this._super.apply(this, arguments);
            this.filterSelection = 'this_week'; // Default filter selection
        },

        start: function () {
            this._renderDashboard();
            return this._super();
        },

        _renderDashboard: function () {
            var self = this;
            this._rpc({
                model: 'my_project_extension.dashboard',
                method: 'get_dashboard_data',
                args: [this.filterSelection],
            }).then(function (result) {
                self.$('.o_dashboard_task_count_value').text(result.task_count);
            });
        },

        _onFilterSelectionChange: function (ev) {
            this.filterSelection = $(ev.target).val();
            this._renderDashboard();
        },
    });
    core.action_registry.add('project_task_dashboard_tag', Dashboard);

    return Dashboard;
});
