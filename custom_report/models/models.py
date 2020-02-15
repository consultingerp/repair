# -*- coding: utf-8 -*-

from odoo import models, fields, api


class CustomReport(models.TransientModel):

    _name = 'custom.reports.report_custom_template'

    @api.model
    def get_report_values(self, docids, data=None):

        docs = []
        docs = self.env['fleet.diagnose'].browse(
            self._context.get('active_id'))

        return {
            'doc_ids': docids,
            'doc_model': 'model.name',
            'docs': docs,
            'data': data,
        }
