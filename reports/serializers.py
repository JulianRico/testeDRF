from rest_framework import serializers
from .models import Report
from users.models import User
from companies.models import Companie



class ReportSerializer (serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    companie = serializers.PrimaryKeyRelatedField(queryset=Companie.objects.all()) 
    class Meta:
        model = Report
        fields = ('id', 'status','questionsmtto','questionviews', 'questionsdeterioration', 'user','companie','create_at')
        read_only_fields = ('create_at',)
        
