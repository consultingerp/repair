# -*- coding: utf-8 -*-
# Part of BrowseInfo. See LICENSE file for full copyright and licensing details.

{
    "name" : "Automobile/Fleet Repair Workshop Service center OpenERP/Odoo 12",
    "version" : "12.0.0.3",
    "category": "Extra Tools",
    "description": """
Manage fleet repairing
==================================

It handles the full repairing workflow:

** fleet Repair ** fleet Diagnosis ** fleet Work Order **

You can choose one more invoicing method here: auto workshop repair , automobile garage ,  automobile Service center, car Service center fleet Service center in odoo , 

* *After Workorder*: A Draft invoice is created and must be paid after workorder completion.
    BrowseInfo developed a new odoo/OpenERP module apps. car workshop
    This module use for autorepair industry , workshop management, Car Repair service industry, Spare parts industry. Fleet repair management. Vehicle Repair shop, Mechanic workshop, Mechanic repair software.Maintenance and Repair car. Car Maintenance Spare Part Supply. Car Servicing, Auto Servicing, Auto mobile Service, Bike Repair Service. Maintenance and Operation.
        
    """,
    "author": "BrowseInfo",
    "website" : "www.browseinfo.in",
    'price': '80.00',
    'currency': "EUR",
    "depends" : ['base', 'sale','sale_management', 'purchase', 'account', 'sale_stock', 'mail', 'product', 'stock', 'fleet', 'website', 'portal'],
    "data" :[
            'security/fleet_repair_security.xml',
            'security/ir_rule.xml',
            'security/ir.model.access.csv',
            'wizard/fleet_repair_assign_to_head_tech_view.xml',
            'wizard/fleet_diagnose_assign_to_technician_view.xml',
            'views/fleet_repair_view.xml',
            'views/product_view.xml',
            'views/fleet_repair_sequence.xml',
            'views/fleet_diagnose_view.xml',
            # 'views/fleet_diagnose_workflow.xml',
            # 'views/fleet_repair_workflow.xml',
            'views/fleet_workorder_sequence.xml',
            'views/fleet_workorder_view.xml',
            # 'views/fleet_workorder_workflow.xml',
            'views/custom_sale_view.xml',
            'report/car_repair_request_fleet.xml',
            'datas/mail_template_ticket.xml',
            'views/feedback.xml',
            'views/thankyou.xml',
            'report/invoice_report.xml',
            'report/sale_order_report.xml',
            'report/fleet_repair_label_view.xml',
            'report/fleet_repair_label_menu.xml',
            'report/fleet_repair_receipt_view.xml',
            'report/fleet_repair_receipt_menu.xml',
            'report/fleet_diagnostic_request_report_view.xml',
            'report/fleet_diagnostic_request_report_menu.xml',
            'report/fleet_diagnostic_result_report_view.xml',
            'report/fleet_diagnostic_result_report_menu.xml',
            'report/fleet_workorder_report_view.xml',
            'report/fleet_workorder_report_menu.xml',

       
        ],
    'qweb':[ ],
    "auto_install": False,
    "installable": True,
    "images":['static/description/Banner.png'],
    'live_test_url':'https://youtu.be/CQwzWEJZuAU',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
