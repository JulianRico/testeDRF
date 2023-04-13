from rest_framework import serializers
from .models import Companie
from reports.serializers import ReportSerializer

class CompanieSerializer (serializers.ModelSerializer):
    reports = ReportSerializer(many=True, required=False)
    class Meta:
        model = Companie
        fields = ('id', 'name','email', 'address', 'phone','nit','manager','create_at', 'reports')
        read_only_fields = ('create_at',)        
        
