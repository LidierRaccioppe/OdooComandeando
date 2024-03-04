# -*- coding: utf-8 -*-
from odoo import fields, models

class PuntosModel(models.Model):
    _name = "puntuacion"
    _description = "Punto Model"

    usuario = fields.Char(string="Usuario")
    puntos = fields.Text(string="Puntos")
