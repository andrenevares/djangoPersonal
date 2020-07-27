from django.shortcuts import render
from django.http import HttpResponse

def questao(request):
    conteudo = {}
    return render (request, 'questionario/questao.html', conteudo)

def detalhe_questao(request, question_id):
    conteudo = {}
    return HttpResponse("Você está vendo a questão número %s." % question_id)

def resultados_questao(request, question_id):
    conteudo = {}
    response = "Você está vendo os resultados da questão número  %s."
    return HttpResponse(response % question_id)

def avaliacao_questao(request, question_id):
    conteudo = {}
    return HttpResponse("Você está votando na questão número  %s." % question_id)