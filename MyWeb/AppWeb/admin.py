from django.contrib import admin
from .models import Article, User, Author
from django_summernote.admin import SummernoteModelAdmin


# Register your models here.
class PostAdmin(SummernoteModelAdmin, admin.ModelAdmin):
    summernote_fields = ('content')  # 给content字段添加富文本
    list_display = ['title', 'author', 'created_time']
    search_fields = ['title']  # 搜索框
    list_filter = ['created_time']  # 过滤器


admin.site.register(Article, PostAdmin)
admin.site.register(User)
admin.site.register(Author)



