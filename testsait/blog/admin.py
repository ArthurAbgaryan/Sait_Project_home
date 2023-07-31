from django.contrib import admin
from blog.models import Post


@admin.register(Post)
class AdminPost(admin.ModelAdmin):
    list_display = ['title','date_created','author']
    prepopulated_fields = {'slug':('title',)}
# Register your models here.
