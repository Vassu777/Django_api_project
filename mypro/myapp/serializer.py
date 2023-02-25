from rest_framework import serializers
from myapp.models import *
class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model= candidate
        fields="__all__"