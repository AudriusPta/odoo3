from odoo import models, fields


class BooksWizard(models.TransientModel):
    _name = 'books.wizard'
    _description = 'Wizard Form'

    data_from = fields.Data('From')
    data_to = fields.Data('To')

    def print_report(self):
        data = {
            'ids': self.ids,
            'model': 'books.wizard',
            'form': {
                'data_from': self.data_from,
                'data_to': self.data_to,
            },
        }
        return self.env.ref('books.print_report_template').report_action(self, data=data)


