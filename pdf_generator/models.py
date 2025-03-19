from django.db import models

from users.models import User

# Create your models here.
class PDFDownload(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True)
    blog = models.ForeignKey("blogs.Blog", on_delete=models.CASCADE, related_name="pdf_downloads")
    downloaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username if self.user else 'Guest'} downloaded {self.blog.title[:30]}"
