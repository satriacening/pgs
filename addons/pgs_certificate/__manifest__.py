{
    "name": "PGS Certificate",
    "version": "17.0.1.0.0",
    "category": "Project",
    "summary": "Certificate for Contact res.partner",
    "author": "Satria Putra | satriacening@gmail.com",
    "depends": [
        "base"
    ],
    "data": [
        "security/ir.model.access.csv",

        "views/pgs_certificate_views.xml",
        "views/action_menuitem.xml",

        "report/pgs_report.xml"
    ],
    "license": "LGPL-3",
    "installable": True,
    "auto_install": False,
    "application": False,
}
