from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.template import loader

# Create your views here.
# request => requisição que é feita no navagador para o back-end
# response => resposta que o back-end devolve para o navegador

def index(request: HttpRequest) -> HttpResponse:
    # Obteve o arquivo templetes/index.html e armazena na variavel template
    template = loader.get_template(template_name="index.html")
    # renderizar o template armazenando na variavel html, ou seja, vai gerar o html
    html = template.render(context={}, request=request)
    # instanciando um objeto da classe httpresponse definindo o que será

    response = HttpResponse(content=html)
    return response


def contato(request: HttpRequest) -> HttpResponse:
    return render(request, "contato.html", context={})


def calculadora(request: HttpRequest) -> HttpResponse:
    return render(request, "calculadora.html", context={})


def calcular(request: HttpRequest) -> HttpResponse:
    # request.GET é o metodo da requisão, quais são possiveis de utilizar:
    # request.GET a informação vai na URL
    # request.POST a informação vai por de baixo dos panos
    # .get => é utilizado para obter um valor
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    soma = numero1 + numero2
    if numero1 > numero2:
        maior = "Primeiro Número"
    else:
        maior = "Segundo Número"

    dados_para_html = {
        "soma": soma,
        "maior": maior,
        "numero1": numero1,
        "numero2": numero2,
    }
    return render(request, "resultado.html", context=dados_para_html)


def aluno(request: HttpRequest) -> HttpResponse:
    return render(request, "aluno.html", context={})


def media(request: HttpRequest) -> HttpResponse:
    nota1 = int(request.GET.get("nota1"))
    nota2 = int(request.GET.get("nota2"))
    nota3 = int(request.GET.get("nota3"))
    media = (nota1 + nota2 + nota3)/3

    if media >= 7:
        situacao = "Aprovado"
    elif media >=5 and media < 7:
        situacao = "Em Exame"
    else:
        situacao = "Reprovado"

    dados_aluno = {
        "nota1": nota1,
        "nota2": nota2,
        "nota3": nota3,
        "media": media,
        "status": situacao        
    }

    return render(request, "calcular-media.html", context=dados_aluno)