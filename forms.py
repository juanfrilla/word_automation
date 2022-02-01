from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, DateField
from wtforms.validators import DataRequired


# create a Form class
class ContractForm(FlaskForm):  # validar para el futuro
    sexo = SelectField("Sexo",
                       choices=[("Don", "Don"), ("Doña", "Doña")],
                       validators=[DataRequired()])
    dni = StringField("DNI",
                      validators=[DataRequired()
                                  ])  # tipo numero y te calcula la letra
    nombre = StringField("Nombre", validators=[DataRequired()])
    apellidos = StringField("Apellidos", validators=[DataRequired()])
    localidad_nacimiento = StringField("Localidad",
                                       validators=[DataRequired()])
    provincia_nacimiento = StringField("Provincia",
                                       validators=[DataRequired()])
    letra = SelectField(
        "Letra",
        choices=[("A", "A"), ("B", "B"), ("C", "C")],
        validators=[DataRequired()],
    )
    precio = SelectField(
        "Precio",
        choices=[("350", "350"), ("450", "450"), ("500", "500")],
        validators=[DataRequired()],
    )  # tipo float
    dormitorios = SelectField("Dormitorios",
                              choices=[("1", "1"), ("2", "2")],
                              validators=[DataRequired()])

    # fecha_hoy = DateField('Fecha hoy', format='%m/%d/%Y', validators=[DataRequired()])
    fecha_hoy = StringField("Fecha hoy", validators=[DataRequired()])
    submit = SubmitField("Submit")
