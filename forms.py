from flask_wtf import FlaskForm
from wtforms import RadioField, StringField, SubmitField
from wtforms.validators import DataRequired, Email


class formcheck(FlaskForm):
    txtP1 = 'Princípios da LGPD: os setores que acessam essas informações têm seus colaboradores atualizados ' \
            'quanto a essa questão?'
    txtP2 = 'Termo de consentimento: seus clientes permitem a utilização de seus próprios dados?'
    txtP3 = 'Termo de responsabilidade: seus clientes sabem para que seus dados serão utilizados?'
    txtP4 = 'Uso de firewalls, criptografia e antivírus: os seus dados (e os de seus clientes) estão realmente seguros?'
    txtP5 = ' Seus parceiros e fornecedores: eles obedecem à LGPD?'
    txtNome = 'Nome'
    txtEmail = 'Email'

    nome = StringField(txtNome, validators=[DataRequired()])
    email = StringField(txtEmail, validators=[DataRequired(), Email()])
    perg1 = RadioField(txtP1, choices=['Sim', 'Nao'], validators=[DataRequired()])
    perg2 = RadioField(txtP2, choices=['Sim', 'Nao'], validators=[DataRequired()])
    perg3 = RadioField(txtP3, choices=['Sim', 'Nao'], validators=[DataRequired()])
    perg4 = RadioField(txtP4, choices=['Sim', 'Nao'], validators=[DataRequired()])
    perg5 = RadioField(txtP5, choices=['Sim', 'Nao'], validators=[DataRequired()])
    btnFinalizar = SubmitField('Finalizar')


class btn(FlaskForm):
    btnFormulario = SubmitField('Preencher formulario')
