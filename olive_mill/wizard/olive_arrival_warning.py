# -*- coding: utf-8 -*-
# Copyright 2018 Barroux Abbey (https://www.barroux.org/)
# @author: Alexis de Lattre <alexis.delattre@akretion.com>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from odoo import fields, models


class OliveArrivalWarning(models.TransientModel):
    _name = 'olive.arrival.warning'
    _description = 'Olive arrivals warning'

    arrival_id = fields.Many2one('olive.arrival', required=True)
    count = fields.Integer(readonly=True)
    msg = fields.Text(readonly=True)

    def validate(self):
        self.arrival_id.with_context(olive_no_warning=True).validate()
        return
