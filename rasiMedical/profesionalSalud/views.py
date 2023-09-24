from django.http import HttpResponse
from .logic import profesionalSalud_logic as pl
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
# Create your views here.

@csrf_exempt
def profesionalesSalud_view(request):
    if request.method == 'GET':
        profs = pl.get_profesionalesSalud()
        profsDTO = serializers.serialize('json', profs)
        return HttpResponse(profsDTO, content_type = 'application/json')


@csrf_exempt
def profesionalSalud_view(request, pk):
    if request.method == 'GET':
        prof = pl.get_profesionalSalud(pk)
        prof_dto = serializers.serialize('json', [prof])
        return HttpResponse(prof_dto, content_type = 'application/json')


