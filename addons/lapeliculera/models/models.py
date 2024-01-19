# -*- coding: utf-8 -*-

from odoo import models, fields, api

# class lapeliculera(models.Model):
#     _name = 'lapeliculera.lapeliculera'
#     _description = 'lapeliculera.lapeliculera'

#     name = fields.Char()
#     value = fields.Integer()
#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100


class lapeliculera_pelicula(models.Model):
    _name = 'lapeliculera.pelicula'
    _description = 'Película'
    name = fields.Char(string="Titulo", required=True, help="Introduce el titulo de la película")
    director = fields.Char(string="Director",required=True, help="Introduce el director")
    color = fields.Boolean(string="Color")
    duracion = fields.Integer(string="Duración en minutos")
    industria = fields.Selection([('0', 'Hollywood'), ('1', 'Bollywood'), ('2', 'Otras')], default="1", string="Industria")
    fecha = fields.Date(string="Fecha de estreno en España")
    sinopsis = fields.Text(string="Sinopsis")

    genero = fields.Many2one("lapeliculera.genero",string="Género",required=True)


class lapeliculera_genero(models.Model):
    _name = 'lapeliculera.genero'
    _description = 'Género cinematográfico'
    name = fields.Char(string = "Género", required=True, help="Introduce el género cinematográfico")
    comentario = fields.Text(string="Comentarios")

    pelicula = fields.One2many("lapeliculera.pelicula", "genero", string="Películas")