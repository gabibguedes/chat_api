from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import Message, User
from .serializers import MessageSerializer, UserSerializer
from django.db.models import Q



@permission_classes([IsAuthenticated])

class MessageViewSet(viewsets.ModelViewSet):
    """API endpoint that allows firmwares to be created, viewed or edited."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_url_kwarg = None


    def list(self, request, **kwargs):
        profile = request.user
        messages_received = Message.objects.filter(Q(receiver=profile.id)).order_by('-id')
        messages_sent = Message.objects.filter(Q(sender=profile.id)).order_by('-id')
        queryset = messages_received | messages_sent

        if 'chat_with' in request.GET:
            chat_with = request.GET['chat_with']
            messages_sent = queryset.filter(
                Q(sender=chat_with)).order_by('-id')
            messages_received = queryset.filter(
                Q(receiver=chat_with)).order_by('-id')
            queryset = messages_received | messages_sent
        
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)
