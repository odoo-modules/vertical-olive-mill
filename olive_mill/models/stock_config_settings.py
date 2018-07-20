# -*- coding: utf-8 -*-
# Copyright 2018 Barroux Abbey (https://www.barroux.org/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).


from odoo import models, fields, api, _
from odoo.exceptions import UserError


class StockConfigSettings(models.TransientModel):
    _inherit = 'stock.config.settings'

#    oil_default_expiry_date = fields.Date(
#        related='company_id.oil_default_expiry_date')