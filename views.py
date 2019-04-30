from django.shortcuts import render, get_object or 404
from .models import TechType, Product, Review

def index (request):
    return render(request, 'techapp/index.html')

def getypes (request):
    types list = TechType.objects.all()
    context {"types_list" : types list}
    return render (request, 'PythonClubApp/types.html' context=context)

def getResouces (request):
    resources list=Resource.objects.all()
    return render (request, 'clubapp.resources.html'), {'resource list': resource list}

def meetingsAgenda (request, id)
prod=Meetings.agenda.get (pk=id)
agenda=Meetings.agenda.filter(meeting=id)
context{
'prod' : prod,
resourcecount: resourcecount,
}

return render (request, "clubapp/resoucedetail.html", context = context)