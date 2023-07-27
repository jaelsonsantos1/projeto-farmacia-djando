from django.core.paginator import Paginator
from medicamentos.models import Medicamentos
from medicamentos.serializers import MedicamentosSerializer
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json


@csrf_exempt
def lista_medicamentos(request):
   # Busca todos os registros do banco
   medicamentos = Medicamentos.objects.all()

   # Limite de itens buscados para se carregar em uma página
   itens_maximo_por_pagina = 10
   
   # Pegando o valor do parâmetro de qual pagina carregar dos dados
   pagina_numero = request.GET.get('pagina', 1)

   # Criando a paginação
   paginator = Paginator(medicamentos, itens_maximo_por_pagina)
   # Pegando a pagina de infomações especifica pelo numero da pagina especificado
   pagina = paginator.get_page(pagina_numero)

   # Serializando os dados buscados para que sejam comvertidos em formato JSON
   medicamentos_data = MedicamentosSerializer(pagina, many=True)
   
   # Convertendo as informações serializados no tipo Python e transformando-as numa string format
   serialized_data = json.dumps(medicamentos_data.data)
   
   # Convertendo o objeto que esta em formato string para dicionário do Python
   python_data = json.loads(serialized_data)

   # Json da resposta
   response_data = {
      'medicamentos': python_data,
      'tem_proxima_pagina': pagina.has_next()
   }

   return JsonResponse(response_data, safe=False)
