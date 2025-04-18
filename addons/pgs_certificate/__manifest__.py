
{
    "name": "PGS Certificate",
    "version": "17.0.1.0.0",
    "category": "Project",
    "summary": "Certificate for Contact res.partner",
    "author": "Satria Putra | satriacening@gmail.com",
    "depends": [
        "base",
        "website"
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/res_partner_views.xml",
        "views/res_users_views.xml",
        "views/pgs_certificate_views.xml",
        "views/res_config_settings_views.xml",
        "views/action_menuitem.xml",
        "views/certificate_search_template.xml",

        "report/pgs_report.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
