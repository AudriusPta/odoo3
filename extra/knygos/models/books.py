from odoo import fields, models, api

class Books(models.Model):
    _name = 'books'
    bookname = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    company = fields.Many2one('company', string='Company')


class Company(models.Model):
    _name = 'company'
    companyname=fields.Char(string='Name', required=True)



