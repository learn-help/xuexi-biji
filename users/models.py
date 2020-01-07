from django.db import models
from django.contrib.auth.models import User

class UserInfo(models.Model):
    """存储用户详细信息的模型"""
    email = models.EmailField(max_length=64)
    check_email = models.BooleanField()
    check_code = models.CharField(max_length=64)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Users info'

    def __str__(self):
        """Return a string representation of the model."""
        return self.email
