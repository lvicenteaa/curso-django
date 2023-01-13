from django.http import HttpResponse

def saludo(request):
    return HttpResponse("Hello Friend")

def bye(request):
    return HttpResponse("Bye Friend")

def adulto(request, edad):
    if edad >= 18:
        return HttpResponse("Eres mayor de edad")
    else:
        return HttpResponse("Eres menor de edad")