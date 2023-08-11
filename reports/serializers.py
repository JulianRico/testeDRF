from rest_framework import serializers
from .models import Report
from users.models import User
from companies.models import Companie, UserCompany


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name', 'address', 'phone', 'email')


class CompanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companie
        fields = ('id', 'name', 'nit', 'email')


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('id', 'usuario', 'address', 'phone',
                  'contact', 'emailContact')


class ReportSerializer(serializers.ModelSerializer):
    user = UserSerializer()
    companie = CompanieSerializer()
    status_display = serializers.SerializerMethodField()
    userCompany = UserCompanySerializer()

    class Meta:
        model = Report
        fields = ('id', 'status_display', 'status', 'questionsmtto', 'questionviews', 'tankidentification', 'observationsandresults', 'signatures',
                  'questionsdeterioration', 'photos', 'user', 'companie', 'userCompany', 'create_at')
        read_only_fields = ('create_at', 'id')

    def get_status_display(self, obj):
        return dict(Report.SelfStatus).get(obj.status)
