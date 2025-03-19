from django.contrib import admin 
from .models import PDFDownload

@admin.register(PDFDownload)
class PDFDownloadAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'blog', 'downloaded_at')  # Columns to display in admin panel
    list_filter = ('downloaded_at', 'user')  # Filter options
    search_fields = ('user__username', 'blog__title')  # Enable search by username and blog title
    ordering = ('-downloaded_at',)  # Order by newest downloads first

