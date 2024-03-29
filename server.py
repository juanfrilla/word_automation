from flask import Flask, render_template
from forms import ContractForm
from formData import FormData

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"


@app.route("/hello", methods=["GET"])
def hello():
    return "Hello"


@app.route("/", methods=["GET", "POST"])
def contract():
    form = ContractForm()
    if form.validate_on_submit():
        output = FormData(
            form.sexo.data,
            form.dni.data,
            form.nombre.data,
            form.apellidos.data,
            form.localidad_nacimiento.data,
            form.provincia_nacimiento.data,
            form.letra.data,
            form.precio.data,
            form.dormitorios.data,
            form.fecha_hoy.data,
        )
        output.genera_contrato()
        return "Contrato generado"
    return render_template("contract.html", form=form)


if __name__ == "__main__":
    app.run()
