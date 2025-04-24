from odoo import fields, models, api


class PgsCertificate(models.Model):
    _name = "pgs.certificate"
    _rec_name = "certification_number"

    instrument_name = fields.Char("Instrument's Name")
    manufacturer = fields.Char('Manufacturer')
    type = fields.Char('Type')
    serial_number = fields.Char('Serial Number')
    detection_principle = fields.Char('Detection Principle')
    location = fields.Char('Location')
    calibration_date = fields.Date('Calibration Date')
    next_calibration_date = fields.Date('Next Calibration')
    certification_number = fields.Char('Certificate Number')
    owner_name = fields.Many2one('res.partner', 'Name')
    # owner_name = fields.Char('Name')
    owner_location = fields.Char('Owner Location')
    page = fields.Integer('Page')
    cylinder_gas = fields.Char('Cylinder Gas')
    traceable_through = fields.Char('Traceable to SI through')
    calibration_procedure = fields.Char('Calibration Procedure')
    inspector = fields.Many2one('res.users','Inspector')
    inspected_date = fields.Date('Inspected Date')
    manufacture_date = fields.Date('Manufacture Date')
    replaced_part = fields.Char('Replaced Part')

    certification_line_ids = fields.One2many('pgs.certificate.line', 'certificate_id')

    signature = fields.Binary(string="Signature", compute="_compute_signature")
    signature_filename = fields.Char(string="Signature Filename", compute="_compute_signature")
    barcode = fields.Binary(string="Barcode", compute="_compute_signature")
    barcode_filename = fields.Char(string="Barcode Filename", compute="_compute_signature")

    @api.depends()
    def _compute_signature(self):
        config = self.env['ir.config_parameter'].sudo()
        signature = config.get_param('pgs_certificate.signature')
        filename = config.get_param('pgs_certificate.signature_filename')
        barcode = config.get_param('pgs_certificate.barcode')
        barcode_filename = config.get_param('pgs_certificate.barcode_filename')
        for rec in self:
            rec.signature = signature
            rec.signature_filename = filename
            rec.barcode = barcode
            rec.barcode_filename = barcode_filename

    def download_certificate(self):
        self.ensure_one()  # pastikan hanya 1 record
        return {
            'type': 'ir.actions.act_url',
            'url': f'/certificate/report/{self.id}',  # URL kamu
            'target': 'new',  # buka di tab baru
        }