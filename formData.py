import os
import sys
from docxtpl import DocxTemplate


class FormData:

    def __init__(
        self,
        sexo,
        dni,
        nombre,
        apellidos,
        localidad_nacimiento,
        provincia_nacimiento,
        letra,
        precio,
        dormitorios,
        fecha_hoy,
    ):
        self.sexo = sexo
        self.dni = dni
        self.nombre = nombre
        self.apellidos = apellidos
        self.localidad_nacimiento = localidad_nacimiento
        self.provincia_nacimiento = provincia_nacimiento
        self.letra = letra
        self.precio = precio
        self.dormitorios = dormitorios
        self.fecha_hoy = fecha_hoy

    def genera_contrato(self):
        os.chdir(sys.path[0])
        doc = DocxTemplate("Plantilla_contrato.docx")
        context = {}

        context["nombre"] = self.nombre
        context["apellidos"] = self.apellidos
        context["dni"] = self.dni
        context["fecha_hoy"] = self.fecha_hoy
        context["localidad_nacimiento"] = self.localidad_nacimiento
        context["provincia_nacimiento"] = self.provincia_nacimiento
        context["sexo"] = self.sexo
        context["letra"] = self.letra
        context["cantidad"] = self.precio
        context["dormitorios"] = self.dormitorios

        doc.render(context)
        doc.save("Contrato_renderizado.docx")


"""
ToDo
# mejorar front-end
# seleccionar la fecha y jugar con el formato fecha.
# si el apartamento es A,B o C. Carga cosas predeterminadas.
# mirar como se pone en negrita algunas cosas.
# Abrir archivo word al final
"""
