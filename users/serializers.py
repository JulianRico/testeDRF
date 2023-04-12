from rest_framework import serializers
from .models import User

class UserSerializer (serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'name','email', 'address', 'phone','about','pictureurl','position','create_at')
        read_only_fields = ('create_at',)
        
