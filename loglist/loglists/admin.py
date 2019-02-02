from django.contrib import admin

# Register your models here.

from .models import Post, Tag

admin.site.register(Tag)

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('text','date_now','switch_ip')
    list_filter = ('date_now', 'switch_ip')
    search_fields=('switch_ip', 'date_now')
