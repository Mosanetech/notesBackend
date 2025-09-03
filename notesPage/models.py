from django.conf import settings
from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=200)
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,  
        on_delete=models.CASCADE,
        related_name='notes'
    )
    attachment = models.FileField(upload_to='notes_attachment/', null=True, blank=True)
    views_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
