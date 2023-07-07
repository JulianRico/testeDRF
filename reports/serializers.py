from rest_framework import serializers
from .models import Report
from users.models import User
from companies.models import Companie


class ReportSerializer (serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        slug_field='name', queryset=User.objects.all())
    status_display = serializers.SerializerMethodField()
   # status  = serializers.SlugRelatedField(slug_field='name', queryset=Report.objects.all())
    companie = serializers.SlugRelatedField(
        slug_field='name', queryset=Companie.objects.all())

    class Meta:
        model = Report
        fields = ('id', 'status_display', 'status', 'questionsmtto', 'questionviews',
                  'questionsdeterioration', 'user', 'companie', 'create_at', )
        read_only_fields = ('create_at', 'id')

    def get_status_display(self, obj):
        return dict(Report.SelfStatus).get(obj.status)
