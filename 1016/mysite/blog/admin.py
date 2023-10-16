from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'content', 'created_at', 'updated_at']
    # fields = ['title', 'content']

admin.site.register(Post, PostAdmin)