from rest_framework import serializers
from .models import Companie, UserCompany
from reports.serializers import ReportSerializer


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('id', 'usuario', 'address', 'phone',
                  'contact', 'emailContact', 'companie', 'create_at')
        read_only_fields = ('create_at',)


class CompanieSerializer (serializers.ModelSerializer):
    reports = ReportSerializer(many=True, required=False)
    users = UserCompanySerializer(many=True, required=False)

    class Meta:
        model = Companie
        fields = ('id', 'name', 'email', 'nit',
                  'create_at', 'reports', 'users')
        read_only_fields = ('create_at',)
