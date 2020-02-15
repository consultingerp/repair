# -*- coding: utf-8 -*-

import base64
from odoo import http, _
from odoo.http import request
from odoo import models,registry, SUPERUSER_ID
from odoo.addons.portal.controllers.portal import CustomerPortal as website_account
import logging
_logger = logging.getLogger(__name__)

class fleet_repair(http.Controller):

    @http.route(['/car_repair_email/feedback/<int:order_id>'], type='http', auth='public', website=True)
    def feedback_email(self, order_id, **kw):
        values = {}
        values.update({'car_ticket_id': order_id})
        return request.render("fleet_repair_management.car_repair_feedback_fleet", values)
       
    @http.route(['/car_repari/feedback/'],
                methods=['POST'], auth='public', website=True)
    def start_rating(self, **kw):
        partner_id = kw['partner_id']
        user_id = kw['car_ticket_id']
        ticket_obj = request.env['fleet.repair'].sudo().browse(int(user_id))
        #if partner_id == UserInput.partner_id.id:
        vals = {
              'rating':kw['star'],
              'comment':kw['comment'],
            }
        ticket_obj.sudo().write(vals)
        customer_msg = _(ticket_obj.client_id.name + 'has send this feedback rating is %s and comment is %s') % (kw['star'],kw['comment'],)
        ticket_obj.sudo().message_post(body=customer_msg)

        #return http.request.render("machine_repair_management.successful_feedback")
        return http.request.render("fleet_repair_management.successful_feedback_car_fleet")

        
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
