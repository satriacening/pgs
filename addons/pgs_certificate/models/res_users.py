from odoo import fields, models


class ResUsers(models.Model):
    _inherit = "res.users"

    signature_certificate = fields.Binary(string="Signature")
    signature_filename = fields.Char(string="Signature Filename")