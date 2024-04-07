from odoo import models, fields, api
from datetime import datetime, timedelta


class Dashboard(models.Model):
    _name = 'my_project_extension.dashboard'
    _description = 'Dashboard'

    project_id = fields.Many2one('project.project', string='Project')
    filter_selection = fields.Selection([
        ('this_week', 'This Week'),
        ('this_month', 'This Month'),
        ('previous_week', 'Previous Week'),
        ('previous_month', 'Previous Month')
    ], string='Filter Selection', default='this_week')

    start_date = fields.Date(string="Start Date", compute="_compute_date_range")
    end_date = fields.Date(string="End Date", compute="_compute_date_range")

    task_count = fields.Integer(string='Task Count', compute='_compute_task_count')

    @api.depends('filter_selection')
    def _compute_date_range(self):
        for record in self:
            if record.filter_selection == 'this_week':
                record.start_date, record.end_date = self._get_this_week_dates()
            elif record.filter_selection == 'this_month':
                record.start_date, record.end_date = self._get_this_month_dates()
            elif record.filter_selection == 'previous_week':
                record.start_date, record.end_date = self._get_previous_week_dates()
            elif record.filter_selection == 'previous_month':
                record.start_date, record.end_date = self._get_previous_month_dates()

    @api.model
    def _get_this_week_dates(self):
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday())
        end_of_week = start_of_week + timedelta(days=6)
        return start_of_week, end_of_week

    @api.model
    def _get_this_month_dates(self):
        today = datetime.now().date()
        start_of_month = today.replace(day=1)
        end_of_month = start_of_month.replace(day=28) + timedelta(days=4)
        return start_of_month, end_of_month - timedelta(days=end_of_month.day)

    @api.model
    def _get_previous_week_dates(self):
        today = datetime.now().date()
        start_of_week = today - timedelta(days=today.weekday(), weeks=1)
        end_of_week = start_of_week + timedelta(days=6)
        return start_of_week, end_of_week

    @api.model
    def _get_previous_month_dates(self):
        today = datetime.now().date()
        start_of_month = today.replace(day=1) - timedelta(days=1)
        end_of_month = start_of_month.replace(day=1)
        return start_of_month, end_of_month - timedelta(days=1)

    @api.depends('project_id', 'start_date', 'end_date')
    def _compute_task_count(self):
        for record in self:
            if record.project_id:
                tasks = self.env['project.task'].search([
                    ('project_id', '=', record.project_id.id),
                    ('create_date', '>=', record.start_date),
                    ('create_date', '<=', record.end_date)
                ])
                record.task_count = len(tasks)
            else:
                record.task_count = 0

    @api.model
    def get_dashboard_data(self, filter_selection):
        start_date, end_date = self._compute_date_range_for_filter(filter_selection)
        tasks = self.env['project.task'].search([
            ('create_date', '>=', start_date),
            ('create_date', '<=', end_date)
        ])
        return len(tasks)

    def _compute_date_range_for_filter(self, filter_selection):
        if filter_selection == 'this_week':
            return self._get_this_week_dates()
        elif filter_selection == 'this_month':
            return self._get_this_month_dates()
        elif filter_selection == 'previous_week':
            return self._get_previous_week_dates()
        elif filter_selection == 'previous_month':
            return self._get_previous_month_dates()
