from django.db import models
from django.contrib.auth.models import User

from .resources import CATEGORY


class Order(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True)
    category = models.CharField(max_length=16, choices=CATEGORY, default='Tank')
    title = models.CharField(max_length=128, verbose_name='title')
    text = models.TextField()
    upload = models.FileField(upload_to='uploads/', blank=True)

    def __str__(self):
        return f"{self.title}"


class Comments(models.Model):
    commentOrder = models.ForeignKey('Order', on_delete=models.CASCADE,
                                     verbose_name='Order',
                                     related_name='comments_orders')
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    dateCreation = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text}"
