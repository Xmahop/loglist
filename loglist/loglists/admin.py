from django.contrib import admin

# Register your models here.

from .models import Post

@admin.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('switch_ip', 'text','date_now')
    list_filter = ('date_now', 'switch_ip')
    search_fields=('switch_ip', 'date_now')
