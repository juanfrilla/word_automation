from docx import Document
from datetime import datetime
import locale


def datetime_to_dateformat(input_date: datetime, format: str):
    locale.setlocale(locale.LC_TIME, "es_ES")
    return input_date.strftime(format)


def remove_blank_pages(filename="./word_docs/Contrato_renderizado.docx"):
    sections_to_remove = []
    doc = Document(filename)
    for i, section in enumerate(doc.sections):
        if (
            not section.footer.paragraphs
            and not section.header.paragraphs
            and not section.paragraphs
        ):
            sections_to_remove.append(i)
    for i in reversed(sections_to_remove):
        doc.element.body.remove(doc.sections[i]._element)
    doc.save(filename)
