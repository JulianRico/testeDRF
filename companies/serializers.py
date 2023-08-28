from rest_framework import serializers
from .models import Companie, UserCompany


class UserCompanySerializer(serializers.ModelSerializer):   
    class Meta:
        model = UserCompany
        fields = ('id', 'usuario')
        


class CompanieSerializer (serializers.ModelSerializer):
    #reports = ReportSerializer(many=True, required=False)
    users = UserCompanySerializer(many=True, required=False)

    class Meta:
        model = Companie
        fields = ('id', 'name', 'email', 'nit',
                  'create_at','users')