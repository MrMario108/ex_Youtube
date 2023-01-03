from django.contrib import admin
from .models import Idea, Vote
from django.utils.html import format_html

# Register your models here.

#admin.site.register(Idea)
#admin.site.register(Vote)

class VoteInLine(admin.StackedInline):
    model = Vote


@admin.register(Idea)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'show_url']
    inlines = [
            VoteInLine
        ]
    def show_url(self, obj):
        if obj.youtube_url is not None:
            return format_html(f'<a target="_blank" href="{obj.youtube_url}">{obj.youtube_url}</a>')
        else:
            return ''

    def __str__(self, obj) -> str:
        return 'ID -',obj.id


@admin.register(Vote)
class IdeaAdmin(admin.ModelAdmin):
    list_display = ['id', 'idea','reason']
    list_filter = ['idea']

    def __str__(self, obj) -> str:
        return 'ID -',obj.id
