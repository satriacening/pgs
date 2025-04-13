# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import api, models, fields


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    signature = fields.Binary(string="Signature")
    signature_filename = fields.Char(string="Signature Filename")

    barcode = fields.Binary(string="Barcode")
    barcode_filename = fields.Char(string="Barcode Filename")

    def set_values(self):
        super(ResConfigSettings, self).set_values()
        self.env['ir.config_parameter'].sudo().set_param('pgs_certificate.signature', self.signature)
        self.env['ir.config_parameter'].sudo().set_param('pgs_certificate.signature_filename', self.signature_filename)
        self.env['ir.config_parameter'].sudo().set_param('pgs_certificate.barcode', self.barcode)
        self.env['ir.config_parameter'].sudo().set_param('pgs_certificate.barcode_filename', self.barcode_filename)

    @api.model
    def get_values(self):
        res = super(ResConfigSettings, self).get_values()
        signature = self.env['ir.config_parameter'].sudo().get_param('pgs_certificate.signature')
        filename = self.env['ir.config_parameter'].sudo().get_param('pgs_certificate.signature_filename')
        barcode = self.env['ir.config_parameter'].sudo().get_param('pgs_certificate.barcode')
        barcode_filename = self.env['ir.config_parameter'].sudo().get_param('pgs_certificate.barcode_filename')
        res.update(
            signature=signature,
            signature_filename=filename,
            barcode=barcode,
            barcode_filename=barcode_filename,
        )
        return res