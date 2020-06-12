from django.shortcuts import render

# Create your views here.

# Django Build in User Model
from django.contrib.auth.models import User
from django.http.response import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
# Our Message model
from chat.models import Message
from chat.serializers import MessageSerializer, UserSerializer  # Our Serializer Classes
# Users View
# Decorator to make the view csrf excempt.
@csrf_exempt
def user_list(request, pk=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        # If PrimaryKey (id) of the user is specified in the url
        if pk:
            # Select only that particular user
            users = User.objects.filter(id=pk)
        else:
            users = User.objects.all()                             # Else get all user list
        serializer = UserSerializer(
            users, many=True, context={'request': request})
        # Return serialized data
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        # On POST, parse the request object to obtain the data in json
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)        # Seraialize the data
        if serializer.is_valid():
            serializer.save()                                            # Save it if valid
            # Return back the data on success
            return JsonResponse(serializer.data, status=201)
        # Return back the errors  if not valid
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def message_list(request, sender=None, receiver=None):
    """
    List all required messages, or create a new message.
    """
    if request.method == 'GET':
        messages = Message.objects.filter(
            sender_id=sender, receiver_id=receiver)
        serializer = MessageSerializer(
            messages, many=True, context={'request': request})
        return JsonResponse(serializer.data, safe=False)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = MessageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)
