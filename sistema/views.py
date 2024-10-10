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
    numero1 = int(request.GET.get("numero1"))
    numero2 = int(request.GET.get("numero2"))
    soma = numero1 + numero2
    dados_para_html = {
        "soma": soma
    }
    return render(request, "resultado.html", context=dados_para_html)