# -*- coding: utf-8 -*-

from odoo import models, fields, api


# class fcties(models.Model):
#     _name = 'fcties.fcties'
#     _description = 'fcties.fcties'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

class alumno(models.Model):
    _name = 'fcties.alumno'
    _description = 'Alumno'

    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    curso_academico = fields.Char(string="Curso academico")
    correo_electronico = fields.Char(string="Correo electronico")
    telefono = fields.Char(string="Teléfono")
    ciclo_formativo = fields.Selection([('0', 'DAM'), ('1', 'DAW'), ('2', 'ASIR')], string="Ciclo formativo", required=True)
    periodo_practica = fields.Selection([('0', 'Abril'), ('1', 'Septiembre')], string="Periodo práctica", required=True)
    nota_media = fields.Float(string="Nota media", required=True)
    nota_media_texto = fields.Char(string="Nota media en texto", compute="_compute_nota_media", store=True)

    empresa = fields.Many2one("fcties.empresa", string="Empresa")

    @api.depends('nota_media')
    def _compute_nota_media(self):
        for alumno in self:
            if alumno.nota_media > 10:
                alumno.nota_media = 10

            if 5 <= alumno.nota_media < 7:
                alumno.nota_media_texto = 'Aprobado'
            elif 7 <= alumno.nota_media < 9:
                alumno.nota_media_texto = 'Notable'
            elif 9 <= alumno.nota_media <= 10:
                alumno.nota_media_texto = 'Sobresaliente'
            else:
                alumno.nota_media_texto = 'Suspendido'


class empresa(models.Model):
    _name = 'fcties.empresa'
    _description = 'Empresa'

    nombre = fields.Char(string="Nombre", required=True)
    persona_contacto = fields.Char(string="Persona de contacto", required=True)
    telefono_contacto = fields.Char(string="Teléfono de contacto", required=True)
    correo_electronico = fields.Char(string="Correo electronico", required=True)
    direccion = fields.Char(string="Dirección", required=True)

    estudiante = fields.One2many("fcties.alumno", "empresa", string="Alumno")
