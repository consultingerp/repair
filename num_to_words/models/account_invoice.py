# -*- coding: utf-8 -*-

from num2words import num2words
from odoo import api, fields, models, _
import logging

_logger = logging.getLogger(__name__)


class AccountInvoice(models.Model):
    _inherit = "account.invoice"

    text_amount = fields.Char(string="Monto en letra",
                              required=False, compute="amount_to_words")
    type_currencychange = fields.Float(
        string="Tasa de cambio", required=False, compute="change_currency")
    type_currencychange_nic = fields.Float(
        string="Tasa de cambio Córdoba", required=False, compute="change_currency_nic")
    type_currencychange_usd = fields.Float(
        string="Tasa de cambio USD", required=False, compute="change_currency_usd")
    # dolar_amount = fields.Float(string="Monto en letra dolar", required=False, compute="amount_to_dolar")

    @api.depends('amount_total')
    def amount_to_words(self):

        for element in self:
            if element.company_id.text_amount_language_currency:
                aux = num2words(element.amount_total,
                                lang=element.company_id.text_amount_language_currency)
                #_logger.info("*******************%r" % element.amount_total)
                monedas = {"NIO": "Córdobas", "COR": "Córdobas", "USD": "Dólares", "EUR": "Euros", "CRC": "Colones",
                           "HNL": "Lempiras"}
                monetary1 = aux.split("punto")
                if element.amount_total == 1:
                    moneda = element.currency_id.currency_unit_label
                else:
                    moneda = monedas[element.currency_id.name]
                #_logger.info("*******************%r" % monetary1)
                l = len(monetary1)
                if l > 1:

                    total = "{0:.2f}".format(element.amount_total)

                    element.text_amount = monetary1[0].capitalize(
                    ) + "con " + (total.split('.'))[1] + '/100' + " " + moneda

                else:

                    element.text_amount = monetary1[0].capitalize(
                    ) + " " + moneda

    # def amount_to_dolar(self):
    #
    #     for element in self:
    #       if element.currency_id.name == "USD":
    #           if element.amount:
    #             element.dolar_amount = element.amount
    #           else:
    #             element.dolar_amount = 0
    #       else:
    #           element.dolar_amount = 0

    def change_currency(self):

        for element in self:

            # currency = self.env['res.currency'].search([('name', '=', 'NIO')])
            currency = element.currency_id

            print(currency.id)

            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.date_due),
            ], order='name asc')

            #print("RATEEEEEEEEEE%r" % rate_crc)

            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00

            element.type_currencychange = rate

    def change_currency_nic(self):
        for element in self:
            currency = self.env['res.currency'].search([('name', '=', 'NIO')])
            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.date_due),
            ], order='name asc')
            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00
            element.type_currencychange_nic = rate

    def change_currency_usd(self):
        for element in self:
            currency = self.env['res.currency'].search([('name', '=', 'USD')])
            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.date_due),
            ], order='name asc')
            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00
            element.type_currencychange_usd = rate


class AccountPayment(models.Model):

    _inherit = 'account.payment'

    text_amount = fields.Char(string="Monto en letra",
                              required=False, compute="amount_to_words")

    type_currencychange = fields.Float(
        string="Tasa de cambio", required=False, compute="change_currency")
    type_currencychange_usd = fields.Float(
        string="Tasa de cambio", required=False, compute="change_currency_usd")

    # dolar_amount = fields.Float(string="Monto en letra dolar", required=False, compute= "amount_to_dolar")

    # def amount_to_dolar(self):
    #
    #     for element in self:
    #       if element.currency_id.name == "USD":
    #           element.dolar_amount = element.amount
    #       else:
    #           element.dolar_amount = 0
    def change_currency_usd(self):
        for element in self:
            currency = self.env['res.currency'].search([('name', '=', 'USD')])
            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.payment_date),
            ], order='name asc')
            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00
            element.type_currencychange_usd = rate

    def change_currency(self):

        for element in self:

            # currency = self.env['res.currency'].search([('name', '=', 'NIO')])
            currency = element.currency_id

            print(currency.id)

            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.payment_date),
            ], order='name asc')

            #print("RATEEEEEEEEEE%r" % rate_crc)

            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00

            element.type_currencychange = rate

    @api.depends('amount')
    def amount_to_words(self):

        for element in self:

            if element.company_id.text_amount_language_currency:

                aux = num2words(element.amount,
                                lang=element.company_id.text_amount_language_currency)

                #_logger.info("*******************%r" % element.amount)

                monedas = {"NIO": "Córdobas", "COR": "Córdobas", "USD": "Dólares", "EUR": "Euros", "CRC": "Colones",
                           "HNL": "Lempiras"}

                monetary1 = aux.split("punto")

                if element.amount == 1:
                    moneda = element.currency_id.currency_unit_label
                else:
                    moneda = monedas[element.currency_id.name]

                #_logger.info("*******************%r" % monetary1)

                l = len(monetary1)

                if l > 1:

                    total = "{0:.2f}".format(element.amount)
                    element.text_amount = monetary1[0].capitalize(
                    ) + "con " + (total.split('.'))[1] + '/100' + " " + moneda

                else:

                    element.text_amount = monetary1[0].capitalize(
                    ) + " " + moneda + " netos"


class PurchaseOrderNTW(models.Model):

    _inherit = 'purchase.order'

    text_amount = fields.Char(string="Monto en letra",
                              required=False, compute="amount_to_words")
    type_currencychange = fields.Float(
        string="Tasa de cambio", required=False, compute="change_currency")

    @api.depends('amount_total')
    def amount_to_words(self):

        for element in self:
            if element.company_id.text_amount_language_currency:
                aux = num2words(element.amount_total,
                                lang=element.company_id.text_amount_language_currency)
                #_logger.info("*******************%r" % element.amount_total)
                monedas = {"NIO": "Córdobas", "COR": "Córdobas", "USD": "Dólares", "EUR": "Euros", "CRC": "Colones",
                           "HNL": "Lempiras"}
                monetary1 = aux.split("punto")
                if element.amount_total == 1:
                    moneda = element.currency_id.currency_unit_label
                else:
                    moneda = monedas[element.currency_id.name]
                #_logger.info("*******************%r" % monetary1)
                l = len(monetary1)
                if l > 1:

                    total = "{0:.2f}".format(element.amount_total)

                    element.text_amount = monetary1[0].capitalize(
                    ) + "con " + (total.split('.'))[1] + '/100' + " " + moneda

                else:

                    element.text_amount = monetary1[0].capitalize(
                    ) + " " + moneda

    def change_currency(self):

        for element in self:

            currency = element.currency_id

            print(currency.id)

            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.date_order),
            ], order='name asc')

            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00

            element.type_currencychange = rate


class SaleOrderNTW(models.Model):

    _inherit = 'sale.order'

    text_amount = fields.Char(string="Monto en letra",
                              required=False, compute="amount_to_words")
    type_currencychange = fields.Float(
        string="Tasa de cambio", required=False, compute="change_currency")

    @api.depends('amount_total')
    def amount_to_words(self):

        for element in self:
            if element.company_id.text_amount_language_currency:
                aux = num2words(element.amount_total,
                                lang=element.company_id.text_amount_language_currency)
                #_logger.info("*******************%r" % element.amount_total)
                monedas = {"NIO": "Córdobas", "COR": "Córdobas", "USD": "Dólares", "EUR": "Euros", "CRC": "Colones",
                           "HNL": "Lempiras"}
                monetary1 = aux.split("punto")
                if element.amount_total == 1:
                    moneda = element.currency_id.currency_unit_label
                else:
                    moneda = monedas[element.currency_id.name]
                #_logger.info("*******************%r" % monetary1)
                l = len(monetary1)
                if l > 1:

                    total = "{0:.2f}".format(element.amount_total)

                    element.text_amount = monetary1[0].capitalize(
                    ) + "con " + (total.split('.'))[1] + '/100' + " " + moneda

                else:

                    element.text_amount = monetary1[0].capitalize(
                    ) + " " + moneda

    def change_currency(self):

        for element in self:

            currency = element.currency_id

            print(currency.id)

            rate_crc = self.env['res.currency.rate'].search([
                ('currency_id', '=', currency.id),
                ('name', '<=', self.date_order),
            ], order='name asc')

            if rate_crc:
                rate = [c.rate for c in rate_crc][-1]
            else:
                rate = 1.00

            element.type_currencychange = rate
