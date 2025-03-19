from django.contrib import admin
from .models import Category, Blog, Comment, Like, BlogShare

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'description')
    search_fields = ('name',)

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'category', 'created_at', 'views')
    search_fields = ('title', 'author__username', 'category__name')
    list_filter = ('created_at', 'category')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'created_at')
    search_fields = ('user__username', 'blog__title', 'content')
    list_filter = ('created_at',)

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'created_at')
    search_fields = ('user__username', 'blog__title')

@admin.register(BlogShare)
class BlogShareAdmin(admin.ModelAdmin):
    list_display = ('id', 'blog', 'shared_by', 'created_at')  # Remove 'shared_to'

