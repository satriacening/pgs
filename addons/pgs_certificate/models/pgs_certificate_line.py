from odoo import fields, models


class PgsCertificateLine(models.Model):
    _name = "pgs.certificate.line"

    certificate_id = fields.Many2one('pgs.certificate',)

    parameter = fields.Char('Parameter')
    measuring_range = fields.Char('Measuring Range')
    calibration_gas = fields.Char('Calibration Gas')
    before_cal = fields.Char('Before Cal.')
    after_cal = fields.Char('After Cal.')
    alarm_point = fields.Char('Alarm Point')
    alarm_work = fields.Char('Alarm Work')
    type_sensor = fields.Char('Type Sensor')