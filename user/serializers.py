from rest_framework.serializers import ModelSerializer
from .models import *

class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class HospitalSerializer(ModelSerializer):
    class Meta:
        model = Hospital
        fields = '__all__'

class CarerSerializer(ModelSerializer):
    class Meta:
        model = Carer
        fields = '__all__'


