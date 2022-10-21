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
    perg1 = RadioField(txtP1, choices=['Sim', 'Nao'], validators=[DataRequired()], description=txtP1)
    perg2 = RadioField(txtP2, choices=['Sim', 'Nao'], validators=[DataRequired()], description=txtP2)
    perg3 = RadioField(txtP3, choices=['Sim', 'Nao'], validators=[DataRequired()], description=txtP3)
    perg4 = RadioField(txtP4, choices=['Sim', 'Nao'], validators=[DataRequired()], description=txtP4)
    perg5 = RadioField(txtP5, choices=['Sim', 'Nao'], validators=[DataRequired()], )
    perg6 = RadioField('Departamento Pessoal', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Departamento Pessoal')
    perg7 = RadioField('Recursos Humanos', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Recursos Humanos')
    perg8 = RadioField('Financeiro', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Financeiro')
    perg9 = RadioField('Marketing', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Marketing')
    perg10 = RadioField('Comercial', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Comercial')
    perg11 = RadioField('Administrativo', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Administrativo')
    perg12 = RadioField('Jurídico', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Jurídico')
    perg13 = RadioField('Compliance', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Compliance')
    perg14 = RadioField('Segurança e Monitoramento', choices=['Internamente', 'Terceirizada'], validators=[DataRequired()], description='Segurança e Monitoramento')
    btnFinalizar = SubmitField('Finalizar')


class btn(FlaskForm):
    btnFormulario = SubmitField('Preencher formulario')
