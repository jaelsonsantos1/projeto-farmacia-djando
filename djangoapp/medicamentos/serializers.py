from rest_framework import serializers
from medicamentos.models import Medicamentos

class MedicamentosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Medicamentos
        fields=('__all__')
