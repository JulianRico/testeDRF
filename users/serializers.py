from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from rest_framework import serializers
from .models import User
from reports.serializers import ReportSerializer


class UserSerializer (serializers.ModelSerializer):
    reports = ReportSerializer(many=True, required=False)

    class Meta:
        model = User
        fields = ('id', 'name', 'email', 'address', 'phone', 'about',
                  'pictureurl', 'position', 'create_at', 'reports')
        read_only_fields = ('create_at',)


# class RegisterUserSerializer(serializers.ModelSerializer):
#     email = serializers.EmailField(required=True, validators=[
#                                    UniqueValidator(queryset=get_user_model().objects.all())])
#     password = serializers.CharField(write_only=True, required=True, validators=[validate_password])

#     class Meta:
#         model = get_user_model()
#         fields = '__all__'
#         extra_kwargs={
#             'password': {'write_only':True, 'min_length':8}
#         }
