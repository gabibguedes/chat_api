from django.contrib import admin

# Register your models here.
from chat.models import Message


class MessageAdmin(admin.ModelAdmin):
    list_display = ('message', 'timestamp', 'sender', 'receiver')

admin.site.register(Message, MessageAdmin)
