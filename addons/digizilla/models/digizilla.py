from odoo import api, fields, models
from datetime import date


class DigizillaTag(models.Model):
    _name = 'digizilla.tag'
    _description = 'Digizilla Tag'

    name = fields.Char(string='Name', required=True)
    color = fields.Integer(string='Color')

    _name_uniq = models.Constraint('unique(name)', 'Tag name must be unique.')

class Digizilla(models.Model):
    _name = 'digizilla.digizilla'
    _description = 'Digizilla'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char(string='Name', required=True, tracking=True)

    gender = fields.Selection(
        selection=[('male', 'Male'), ('female', 'Female')],
        string='Gender',
    )

    country_id = fields.Many2one(
        comodel_name='res.country',
        string='Country',
    )

    birth_date = fields.Date(string='Birth Date')

    age = fields.Float(
        string='Age',
        compute='_compute_age',
        store=True,
    )

    tag_ids = fields.Many2many(
        comodel_name='digizilla.tag',
        string='Tags',
    )

    customer_ids = fields.Many2one(
        comodel_name='res.partner',
        string='Customer',
        required=True,
    )

    sale_order_count = fields.Float(
        string='No. of Sales Orders',
        compute='_compute_sale_order_count',
    )

    notes = fields.Html(string='Notes')
    comments = fields.Char(string='Comments')

    @api.depends('birth_date')
    def _compute_age(self):
        today = date.today()
        for record in self:
            if record.birth_date:
                years = today.year - record.birth_date.year - (
                    (today.month, today.day) < (record.birth_date.month, record.birth_date.day)
                )
                record.age = years
            else:
                record.age = 0

    @api.depends('customer_ids')
    def _compute_sale_order_count(self):
        SaleOrder = self.env['sale.order']
        for record in self:
            if record.customer_ids:
                record.sale_order_count = SaleOrder.search_count(
                    [('partner_id', '=', record.customer_ids.id)]
                )
            else:
                record.sale_order_count = 0