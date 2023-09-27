from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/analises')
def mostra_analises():
    return render_template('analises.html')

@app.route('/medidas')
def mostra_medidas():
    return render_template('medidas.html')

@app.route('/contatos')
def mostra_contatos():
    return render_template('contatos.html')

if __name__ == "__main__":
    app.run(debug=True)