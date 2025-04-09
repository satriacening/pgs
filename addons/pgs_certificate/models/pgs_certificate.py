from odoo import fields, models


class PgsCertificate(models.Model):
    _name = "pgs.certificate"

    instrument_name = fields.Char("Instrument's Name")
    manufacturer = fields.Char('Manufacturer')
    type = fields.Char('Type')
    serial_number = fields.Char('Serial Number')
    detection_principle = fields.Char('Detection Principle')
    location = fields.Char('Location')
    calibration_date = fields.Date('Calibration Date')
    next_calibration_date = fields.Date('Next Calibration')
    certification_number = fields.Char('Certificate Number')
    owner_name = fields.Char('Name')
    owner_vessel = fields.Char('Vessel')
    page = fields.Integer('Page')
    cylinder_gas = fields.Char('Cylinder Gas')
    traceable_through = fields.Char('Traceable to SI through')
    calibration_procedure = fields.Char('Calibration Procedure')
    inspector = fields.Char('Inspector')
    inspected_date = fields.Date('Inspected Date')

    certification_line_ids = fields.One2many('pgs.certificate.line', 'certificate_id')