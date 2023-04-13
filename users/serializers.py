from rest_framework import serializers
from .models import User
from reports.serializers import ReportSerializer


class UserSerializer (serializers.ModelSerializer):
    reports = ReportSerializer(many=True, required=False)
    class Meta:
        model = User
        fields = ('id', 'name','email', 'address', 'phone','about','pictureurl','position','create_at', 'reports')
        read_only_fields = ('create_at',)
        
