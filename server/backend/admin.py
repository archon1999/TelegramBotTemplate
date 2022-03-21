from django.contrib import admin

from .models import BotUser, Template


@admin.register(BotUser)
class BotUserAdmin(admin.ModelAdmin):
    list_display = ['id', 'chat_id', 'get_full_name', 'username',
                    'lang']
    list_filter = ['lang']
    search_fields = ['first_name', 'last_name', 'username']


@admin.register(Template)
class TemplateAdmin(admin.ModelAdmin):
    list_display = ['id', 'type', 'title']
