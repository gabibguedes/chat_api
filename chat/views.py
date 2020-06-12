from rest_framework import viewsets, mixins, status
from rest_framework.response import Response
from rest_framework.decorators import permission_classes, action
from rest_framework.permissions import IsAuthenticated
from rest_framework.status import HTTP_404_NOT_FOUND
from .models import Message, User
from .serializers import MessageSerializer, ChatWithSerializer
from django.db.models import Q



@permission_classes([IsAuthenticated])
class MessageViewSet(mixins.CreateModelMixin,
                     mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin,
                     mixins.ListModelMixin,
                     viewsets.GenericViewSet):
    """API endpoint that allows firmwares to be created, viewed or edited."""

    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    lookup_url_kwarg = None


    def list(self, request, **kwargs):
        profile = request.user
        messages_received = Message.objects.filter(Q(receiver=profile.id)).order_by('-timestamp')
        messages_sent = Message.objects.filter(Q(sender=profile.id)).order_by('-timestamp')
        queryset = messages_received | messages_sent

        if 'chat_with' in request.GET:
            chat_with = request.GET['chat_with']
            colleague = User.objects.get(username=chat_with)
            messages_sent = queryset.filter(
                Q(sender=colleague.id)).order_by('-timestamp')
            messages_received = queryset.filter(
                Q(receiver=colleague.id)).order_by('-timestamp')
            queryset = messages_received | messages_sent
        
        serializer = MessageSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def perform_create(self, serializer):
        serializer.save(sender=self.request.user)


@permission_classes([IsAuthenticated])
class UsersImChattingWithViewSet(viewsets.GenericViewSet):
    serializer_class = ChatWithSerializer

    def get_user_from_messages(self, messages_query, role):
        friends = []
        for message in messages_query:
            friend = User.objects.get(username=getattr(message, role))
            friends.append(friend)
        return friends

    def get_queryset(self):
        user = self.request.user
        chat_list = []
        messages_received = Message.objects.filter(
            Q(receiver=user.id)).order_by('-timestamp')

        chat_list = set(self.get_user_from_messages(messages_received, 'sender'))

        messages_sent = Message.objects.filter(
            Q(sender=user.id)).order_by('-timestamp')

        chat_list.update(self.get_user_from_messages(messages_sent, 'receiver'))

        return chat_list

    def list(self, request, **kwargs):
        serializer = ChatWithSerializer(self.get_queryset(), many=True)
        return Response(serializer.data)
            
