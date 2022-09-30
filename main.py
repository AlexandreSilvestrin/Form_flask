from flask import Flask, render_template, url_for, request, flash, redirect
from forms import formcheck ,btn

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
        flash('Formulario Salvo')
        print(f'nome : {forms.nome.data}')
        print(f'email : {forms.email.data}')
        print(f'perg1 : {forms.perg1.data}')
        print(f'perg2 : {forms.perg2.data}')
        print(f'perg3 : {forms.perg3.data}')
        print(f'perg4 : {forms.perg4.data}')
        print(f'perg5 : {forms.perg5.data}')
    return render_template('forms.html', forms=forms)


if __name__ == '__main__':
    app.run(debug=True)
