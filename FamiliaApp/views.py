from this import d
from django.shortcuts import render
from .models import Familiar
from django.template import loader
from django.http import HttpResponse

def fam(request):
    padre=Familiar(nombre="Tomas", edad=42, fecha='1980-09-23')
    madre=Familiar(nombre="Olga", edad=40, fecha='1982-03-02')
    hermana=Familiar(nombre="Rebeca", edad=15, fecha='2006-01-24')
    padre.save()
    madre.save()
    hermana.save()

    listnom=[padre.nombre, madre.nombre, hermana.nombre]
    listage=[padre.edad, madre.edad, hermana.edad]
    listdate=[padre.fecha, madre.fecha, hermana.fecha]

    plantilla=loader.get_template("index.html")
    dicc={'Nombres': listnom, 'Edades': listage, 'Fechas': listdate}
    doc=plantilla.render(dicc)

    return HttpResponse(doc)

