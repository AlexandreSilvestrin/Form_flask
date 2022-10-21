from forms import formcheck
from pathlib import Path


def criarRelatorio():
    forms = formcheck()
    nome = forms.nome.data
    email = forms.email.data
    resp1 = forms.perg1.data
    resp2 = forms.perg2.data
    resp3 = forms.perg3.data
    resp4 = forms.perg4.data
    resp5 = forms.perg5.data
    resp6 = forms.perg6.data
    resp7 = forms.perg7.data
    resp8 = forms.perg8.data
    resp9 = forms.perg9.data
    resp10 = forms.perg10.data
    resp11 = forms.perg11.data
    resp12 = forms.perg12.data
    resp13 = forms.perg13.data
    resp14 = forms.perg14.data


'''relatorio.write(
nome = {forms.perg1.description} 

{resp1}

{forms.perg2.description}

{resp2}

{forms.perg3.description}

{resp3}

{forms.perg4.description}

{resp4}

{forms.perg5.description}

{resp5}

{forms.perg6.description}

{resp6}

{forms.perg7.description}

{resp7}

{forms.perg8.description}

{resp8}

{forms.perg9.description}

{resp9}

{forms.perg10.description}

{resp10}

{forms.perg11.description}

{resp11}

{forms.perg12.description}{resp12}
{forms.perg13.description} = {resp13}
{forms.perg14.description} = {resp14}
)

'''
