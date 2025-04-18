from odoo import http
from odoo.http import request
import base64

class CertificateSearchController(http.Controller):

    @http.route('/api/test', csrf=False, type='http', auth='public', methods=['GET'])
    def test_endpoint(self):
        return "Endpoint is working!"

    @http.route('/certificate/search', type='http', auth='public', website=True)
    def certificate_search(self, **kwargs):
        cert_no = kwargs.get('certification_number')
        serial_no = kwargs.get('serial_number')
        instrument = kwargs.get('instrument_name')
        wa_number = request.env['ir.config_parameter'].sudo().get_param('pgs_certificate.wa_number')

        domain = []
        if cert_no:
            domain.append(('certification_number', 'ilike', cert_no))
        if serial_no:
            domain.append(('serial_number', 'ilike', serial_no))
        if instrument:
            domain.append(('instrument_name', 'ilike', instrument))

        results = request.env['pgs.certificate'].sudo().search(domain) if domain else []

        return request.render('pgs_certificate.certificate_search_template', {
            'certification_number': cert_no or '',
            'serial_number': serial_no or '',
            'instrument_name': instrument or '',
            'wa_number': wa_number,
            'results': results
        })

    @http.route('/certificate/report/<int:cert_id>', type='http', auth='public', website=True)
    def download_certificate_report(self, cert_id, **kwargs):
        certificate = request.env['pgs.certificate'].sudo().browse(cert_id)
        if not certificate.exists():
            return request.not_found()

        pdf = request.env['ir.actions.report'].sudo()._render_qweb_pdf(
            'pgs_certificate.action_report_pgs_certificate', [cert_id]
        )[0]

        filename = f"Certificate-{certificate.certification_number or 'report'}.pdf"
        return request.make_response(pdf, [
            ('Content-Type', 'application/pdf'),
            ('Content-Disposition', f'attachment; filename="{filename}"')
        ])