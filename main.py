from flask import Flask, render_template, url_for, request, flash, redirect
from forms import formcheck, btn, criarRelatorio
app = Flask(__name__)
app.config['SECRET_KEY'] = 'dc9b08d33bd9c8dbf72a933a368352c8'


@app.route('/', methods=['GET', 'POST'])
def home():
    btnn = btn()
    if btnn.validate_on_submit() and 'btnFormulario' in request.form:
        print('clicado')
        return redirect(url_for('form'))
    return render_template('home.html', btn=btnn)


@app.route('/forms', methods=['GET', 'POST'])
def form():
    forms = formcheck()
    if forms.validate_on_submit() and 'btnFinalizar' in request.form:
        # verifica se o botao foi precisonado com td preenchido(validators do forms erificar se esta preenchido)
        global lista, sit
        lista = criarRelatorio(1)
        sit = criarRelatorio(2)
        return redirect(url_for('result'))
    return render_template('forms.html', forms=forms)


@app.route('/forms/results')
def result():
    global lista, sit
    forms = formcheck()
    return render_template('result.html', forms=forms, resps=lista, sit=sit)


if __name__ == '__main__':
    app.run(debug=True)
