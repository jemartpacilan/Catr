from django.contrib import admin

from .models import Message


# Register your models here.
class MessageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['caterer']}),
        (None, {'fields': ['consumer']}),
        (None, {'fields': ['message_body']}),
        (None, {'fields': ['message_owned_by_consumer']}),
    ]


admin.site.register(Message, MessageAdmin)
