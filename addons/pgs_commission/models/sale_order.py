from odoo import fields, models


class SaleOrder(models.Model):
    _inherit = "sale.order"

    po_number = fields.Char('PO Number')