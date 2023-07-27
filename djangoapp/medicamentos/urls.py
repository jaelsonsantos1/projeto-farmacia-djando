from django.urls import path
from . import views

app_name = "medicamentos"

urlpatterns = [
    path('medicamentos/lista_medicamentos/', views.lista_medicamentos, name='lista_medicamentos'),
]
