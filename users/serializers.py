from rest_framework import serializers
from .models import User
from rest_framework.validators import UniqueValidator

class UserSerializer(serializers.ModelSerializer):
    username = serializers.CharField(
        validators=[
            UniqueValidator(
                queryset=User.objects.all(),
                message="A user with that username already exists.",
            )
        ],
    )
    email = serializers.EmailField(
        validators=[UniqueValidator(queryset=User.objects.all())],
    )
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'password', 'full_name', 'artistic_name']
        extra_kwargs = {
            'id': {'read_only': True},
            'password': {'write_only': True}
        }
        

    def create(self, validated_data: dict) -> User:
         return User.objects.create_user(**validated_data)
    
    def update(self, instance: User, validated_data: dict) -> User:
        password = validated_data.pop('password', None)
        if password:
            instance.set_password(password)
        for key, value in validated_data.items():
            setattr(instance, key, value)

        instance.save()

        return instance