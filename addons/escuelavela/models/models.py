# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class escuelavela(models.Model):
#     _name = 'escuelavela.escuelavela'
#     _description = 'escuelavela.escuelavela'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class escuelavela(models.Model):
    _name = 'escuelavela.escuelavela'
    _description = 'Escuela Vela'

    name = fields.Char(string="Denominación", required=True, help="Introduce la denominación de la escuela")
    logotype = fields.Binary(string="Logotipo", help="Introduce el logotipo de la escuela")
    phone = fields.Integer(string="Teléfono", help="Introduce el teléfono de contacto")
    email = fields.Text(string="Email", help="Introduce el correo de contacto")

    monitors = fields.Many2many("escuelavela.monitor", string="Monitores")
    course = fields.One2many("escuelavela.curso", "school", string="Curso")
    student = fields.One2many("escuelavela.alumno", "school", string="Alumno")


class cursos(models.Model):
    _name = 'escuelavela.curso'
    _description = 'Curso'

    title = fields.Char(string="Título", required=True, help="Introduce el nombre del título")
    durationDays = fields.Integer(string="Duración en días")
    durationHours = fields.Integer(string="Duración en horas")
    price = fields.Float(string="Precio")

    school = fields.Many2one("escuelavela.escuelavela", string="Curso")

class monitores(models.Model):
    _name = 'escuelavela.monitor'
    _description = 'Monitor'

    id = fields.Integer(string="ID", required="True")
    name = fields.Char(string="Nombre")
    phone = fields.Integer(string="Teléfono")
    email = fields.Text(string="Email")

    schools = fields.Many2many("escuelavela.escuelavela", string="Escuela")

class alumnos(models.Model):
    _name = 'escuelavela.alumno'
    _description = 'Alumno'

    enrolmentNum = fields.Text(string="Número de mátricula", required=True)
    name = fields.Char(string="Nombre del alumno")
    phone = fields.Integer(string="Teléfono")
    email = fields.Text(string="Email")

    school = fields.Many2one("escuelavela.escuelavela", string="Escuela")