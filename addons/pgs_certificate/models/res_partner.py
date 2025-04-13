from odoo import fields, models


class PgsCertificate(models.Model):
    _inherit = "res.partner"

    certificate_ids = fields.One2many('pgs.certificate', 'owner_name')