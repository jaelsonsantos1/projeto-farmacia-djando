# from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from medicamentos.models import Medicamentos
from medicamentos.serializers import MedicamentosSerializer

@csrf_exempt
def medicamentoApi(request,id=0):
    if request.method=='GET':
        medicamentos = Medicamentos.objects.all()
        medicamentos_serializer = MedicamentosSerializer(medicamentos, many=True)
        print(medicamentos_serializer)
        return JsonResponse(medicamentos_serializer.data, safe=False)
    else:
        return JsonResponse({'Status':'Erro!'}, safe=False)