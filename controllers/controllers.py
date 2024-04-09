from odoo import http
from odoo.http import request, route

class OwlPlayground(http.Controller):
    @http.route(['/dashboard'], type='http', auth='public')
    def show_playground(self):
        """
        Renders the owl playground page
        """
        print("hello  shamim")
        return request.render('my_project_extension.dashboard')
