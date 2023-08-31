from rest_framework import serializers
from .models import Companie, UserCompany


class UserCompanySerializer(serializers.ModelSerializer):   
    class Meta:
        model = UserCompany
        fields = ('id', 'usuario','companie')
        


class CompanieSerializer(serializers.ModelSerializer):
    #reports = ReportSerializer(many=True, required=False)
    users = UserCompanySerializer(many=True, required=False)

    class Meta:
        model = Companie
        fields = ('id', 'name', 'email', 'nit',
                  'create_at','users')


class SetUserCompanySerializar(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('id', 'usuario', 'address', 'phone', 'city',
                  'contact', 'emailContact', 'create_at', 'companie')
        read_only_fields = ('create_at',)                 