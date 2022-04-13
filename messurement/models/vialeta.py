# -*- coding: utf-8 -*-
from odoo import api, fields, models

class messurement_vialeta(models.Model):
    _name = "messurement_vialeta.type"
    _description = "Messurement Vialeta"

    name = fields.Char(string='Name', required=True, translate=True)
    messuremente1 = fields.Char(string='Messurement 1', required=True, translate=True)
    messuremente2 = fields.Char(string='Messurement 2', required=True, translate=True)
    note = fields.Text(string='Description')