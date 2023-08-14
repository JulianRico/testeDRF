from rest_framework import serializers
from .models import Report
from users.models import User
from companies.models import Companie, UserCompany


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id',)


class CompanieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Companie
        fields = ('id',)


class UserCompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCompany
        fields = ('id',)


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

    def create(self, validated_data):
        user_data = validated_data.pop('user')
        companie_data = validated_data.pop('companie')
        user_company_data = validated_data.pop('userCompany')

        user, _ = User.objects.get_or_create(**user_data)
        companie, _ = Companie.objects.get_or_create(**companie_data)
        user_company, _ = UserCompany.objects.get_or_create(
            **user_company_data)

        report = Report.objects.create(
            user=user,
            companie=companie,
            userCompany=user_company,
            **validated_data
        )

        return report
