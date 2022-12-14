from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


def criarRelatorio(x):
    forms = formcheck()
    nome = forms.nome.data
    email = forms.email.data
    perg1 = forms.perg1.description
    resp1 = forms.perg1.data
    perg2 = forms.perg2.description
    resp2 = forms.perg2.data
    perg3 = forms.perg3.description
    resp3 = forms.perg3.data
    perg4 = forms.perg4.description
    resp4 = forms.perg4.data
    perg5 = forms.perg5.description
    resp5 = forms.perg5.data
    perg6 = forms.perg6.description
    resp6 = forms.perg6.data
    perg7 = forms.perg7.description
    resp7 = forms.perg7.data
    if x == 1:
        return [resp1, resp2, resp3, resp4, resp5, resp6, resp7]
    else:
        if 'Não' in (resp1, resp2, resp3, resp4, resp5, resp6, resp7):
            return True
        else:
            return False


class formcheck(FlaskForm):
    txtP1 = 'A empresa solicita o consentimento do titular para tratar seus dados pessoais?'
    txtP2 = 'O tratamento dos dados é realizado para a finalidade que foi previamente comunicada ao titular?'
    txtP3 = 'A empresa possui práticas de governança relacionadas à proteção de dados?'
    txtP4 = 'Existe um responsável na empresa pela proteção dos dados pessoais?'
    txtP5 = 'Há alguma cláusula de prevenção de judicialização de conflitos nos contratos, termos de uso ou termos de consentimento?'
    txtP6 = 'Você tem conhecimento de que a empresa já tenha sido vítima de vazamento de dados pessoais?'
    txtP7 = 'A tecnologia disponível na empresa possibilita a anonimização de dados pessoais?'
    txtNome = 'Nome'
    txtEmail = 'Email'

    nome = StringField(txtNome, validators=[DataRequired()])
    email = StringField(txtEmail, validators=[DataRequired(), Email()])
    perg1 = RadioField(txtP1, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP1)
    perg2 = RadioField(txtP2, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP2)
    perg3 = RadioField(txtP3, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP3)
    perg4 = RadioField(txtP4, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP4)
    perg5 = RadioField(txtP5, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP5)
    perg6 = RadioField(txtP6, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP6)
    perg7 = RadioField(txtP7, choices=['Sim', 'Não'], validators=[DataRequired()], description=txtP7)
    btnFinalizar = SubmitField('Finalizar')


class btn(FlaskForm):
    btnFormulario = SubmitField('Preencher formulario')
