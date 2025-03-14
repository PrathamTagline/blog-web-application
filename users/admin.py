from django.contrib import admin
from .models import User  

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'is_active', 'created_at')  # Customize the admin panel display
    search_fields = ('username', 'email')  # Enable search functionality
    list_filter = ('is_active', 'created_at')  # Add filtering options
    readonly_fields = ('created_at', 'updated_at')  # Make timestamps read-only
