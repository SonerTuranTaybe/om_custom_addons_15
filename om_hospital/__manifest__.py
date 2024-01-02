# -*- coding: utf-8 -*-
{
    'name': 'Hospital Management  ',
    'version': '2.5.0',
    'summary': 'Odoo 15 Development Tutorials',
    'sequence': -100,
    'description': """Odoo 15 Development Tutorials""",
    'category': 'Tutorials',
    'author': 'Odoo Mates',
    'maintainer': 'Odoo Mates',
    'license': 'AGPL-3',
    'depends': ['base_setup', 'product', 'analytic', 'portal', 'digest', 'mail'],
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/male_patient_view.xml',
        'views/appointment_view.xml',
        'views/report_view.xml',
        "reports/report.xml",
        "reports/patient_card.xml"
    ],
    'demo': [],
    'qweb': [],
    'installable': True,
    'application': True,
    'auto_install': False,
}
