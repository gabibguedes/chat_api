from django.contrib.auth.models import User
from rest_framework import serializers
from chat.models import Message


class ChatWithSerializer(serializers.ModelSerializer):
    """For Serializing Chats withs Users """

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name']


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

