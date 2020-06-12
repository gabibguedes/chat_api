from django.urls import path
from . import views
urlpatterns = [
    # URL form : "/api/messages/1/2"
    # For GET request.
    path('api/messages/<int:sender>/<int:receiver>',
         views.message_list, name='message-detail'),
    # URL form : "/api/messages/"
    path('api/messages/', views.message_list,
         name='message-list'),   # For POST
    # URL form "/api/users/1"
    # GET request for user with id
    path('api/users/<int:pk>', views.user_list, name='user-detail'),
    # POST for new user and GET for all users list
    path('api/users/', views.user_list, name='user-list'),
]
