from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', )


class NewsArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'source_name', 'published_at', 'display_category')


class CommentAdmin(admin.ModelAdmin):
    list_display = ('article', 'user', 'created_at')
    list_filter = ('created_at', )


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.NewsArticle, NewsArticleAdmin)
admin.site.register(models.Comment, CommentAdmin)
