from rest_framework import serializers
from .models import Students
class StudentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Students
        fields = '__all__' # Field yang ingin kamu expose di API