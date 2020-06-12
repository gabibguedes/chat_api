from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message


class UserSerializer(serializers.ModelSerializer):
    """For Serializing User"""
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'password']


class MessageSerializer(serializers.ModelSerializer):
    """For Serializing Message"""

    sender = serializers.SlugRelatedField(
        many=False,
        read_only=True,
        slug_field='username'
    )

    receiver = serializers.SlugRelatedField(
        many=False,
        slug_field='username',
        queryset=User.objects.all()
    )

    class Meta:
        model = Message
        fields = ['id', 'sender', 'receiver', 'message', 'timestamp']
        read_only_fields = ['sender']
