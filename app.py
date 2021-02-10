from flask import Flask, render_template, request

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0


@app.route("/")
def index():
	return render_template('index.html')


@app.route('/calculate', methods['GET', 'POST'])
def Counter():
    if request.method == 'POST':
        horaEntrada = request.form['entrada']
        horaSaida = request.form['saida']

        enviar = counter(horaEntrada,horaSaida)
        return enviar


if __name__ == '__main__':
	app.run(debug=True, port=5005)