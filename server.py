from flask import Flask, render_template, request
from forms import ContractForm
from formData import FormData

app = Flask(__name__)
app.config["SECRET_KEY"] = "supersecretkey"


# Create name page
@app.route("/", methods=["GET", "POST"])
def contract():
    form = ContractForm()
    if request.method == "POST" and form.validate():
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
        return "Contrato generado"  # puede que mejore esto y que me lo devuelva en la template
    return render_template("contract.html", form=form)


if __name__ == "__main__":
    app.run()
