
from odoo import models, fields, api

class Alumno(models.Model):
    _name = 'conv25.alumno'
    _description = 'Alumnos para convalidaciones'

    name = fields.Char(string="Nombre y Apellidos", required=True)
    edad = fields.Integer(string="Edad")
    convalidacion_ids = fields.One2many('conv25.convalidacion', 'alumno_id', string="Convalidaciones")

class Modulo(models.Model):
    _name = 'conv25.modulo'
    _description = 'Módulos formativos'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    ciclo_ids = fields.Many2many('conv25.ciclo', string="Ciclos")

class Convalidacion(models.Model):
    _name = 'conv25.convalidacion'
    _description = 'Convalidaciones de alumnos'

    name = fields.Char(string="Referencia")
    fecha_convalidacion = fields.Date(string="Fecha", default=fields.Date.today)
    modulo_id = fields.Many2one('conv25.modulo', string="Módulo", required=True)
    alumno_id = fields.Many2one('conv25.alumno', string="Alumno", required=True)

class Ciclo(models.Model):
    _name = 'conv25.ciclo'
    _description = 'Ciclos formativos'

    name = fields.Char(string="Nombre", required=True)
    description = fields.Text(string="Descripción")
    modulo_ids = fields.Many2many('conv25.modulo', string="Módulos")
            