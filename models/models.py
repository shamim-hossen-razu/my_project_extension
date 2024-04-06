from odoo import models, fields, api


class Team(models.Model):
    _name = 'my_project_extension.team'
    _description = 'Team'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    member_ids = fields.Many2many('res.users', string='Members')
    project_ids = fields.One2many('project.project', 'team_id', string='Projects')


class Project(models.Model):
    _inherit = 'project.project'

    team_id = fields.Many2one('my_project_extension.team', string='Team')
