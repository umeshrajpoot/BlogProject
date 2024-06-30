from django.contrib import admin
from .models import Blog_Post,BlogPost
# Register your models here.
@admin.register(Blog_Post)
class blogadmin(admin.ModelAdmin):
    list_display=['id','title','desc']

@admin.register(BlogPost)
class blogadmin(admin.ModelAdmin):
    list_display=['id','username','title','desc']
