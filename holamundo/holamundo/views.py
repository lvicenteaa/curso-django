from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hello Friend")

def bye(request):
    return HttpResponse('Bye Friend')