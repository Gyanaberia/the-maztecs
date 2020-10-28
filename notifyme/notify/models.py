from django.db import models
from django.utils.timezone import now

class Notification(models.Model):
    instructor = models.CharField(max_length=100)
    course = models.CharField(max_length=100)
    created_at = models.DateTimeField(default=now)
    def __str__(self):
        return f'{self.body}'
    class Meta:
        ordering = ['-created_at']
