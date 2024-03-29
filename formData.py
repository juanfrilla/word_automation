import os
import sys
from docxtpl import DocxTemplate
from utils import datetime_to_dateformat, remove_blank_pages, find_and_complete_dots


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
        doc = DocxTemplate("./word_docs/Plantilla_contrato.docx")
        context = {}

        context["nombre"] = self.nombre
        context["apellidos"] = self.apellidos
        context["dni"] = self.dni
        context["fecha_hoy"] = datetime_to_dateformat(self.fecha_hoy, "%d de %B de %Y")
        context["localidad_nacimiento"] = self.localidad_nacimiento
        context["provincia_nacimiento"] = self.provincia_nacimiento
        context["sexo"] = self.sexo
        context["letra"] = self.letra
        context["cantidad"] = self.precio
        context["dormitorios"] = self.dormitorios

        doc.render(context)
        doc = remove_blank_pages(doc)
        #doc = find_and_complete_dots(doc)
        doc.save("./word_docs/Contrato_renderizado.docx")


