from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Comment(models.Model):
    comment = models.TextField()
    author = models.ForeignKey(User)
    class Meta:
        permissions = (
            ("can_read", "Can read"),
            ("can_comment", "Can comment"),
        )
