from django.http import HttpResponse
import datetime
from django.template import Template,Context


def saludo(respuest):
    nombre="Vladimir"
    apellido="ascue"
    ahora=datetime.datetime.now()


    doc_ecterno=open("C:/Users/samue/OneDrive/Documentos/DJANGO/proyecto/proyecto/plantilla/miplantilla.html")
    plt=Template(doc_ecterno.read())
    doc_ecterno.close()
    ctx=Context({"nombre_persona":nombre, "apellido_persona":apellido, "momento_actual":ahora })
    documento=plt.render(ctx)

    return HttpResponse(documento)

def calcularedad(request, agno):
    return HttpResponse("hyol como estan aqui vamos con ganas")


def damefecha(request):

    fecha_actual=datetime.datetime.now()


    documento="""<html>
    <body>
    <h1>
    fecha hora actual %s
    </h1>
    </body>
    </html>"""% fecha_actual

    return HttpResponse(documento)


def caledad(request,agno):

    edaactual=18
    periodo=agno-2019
    edadfotura=edaactual+periodo

    documento="<html><body><h2>en el año %s  tendras %s años" %(agno, edadfotura)

    return HttpResponse(documento)
