from django.db import models
from django.conf import settings

class Post(models.Model):
    title = models.CharField(max_length=100)
    contents = models.TextField()
    auth = models.CharField(max_length=20)
    main_image = models.ImageField(upload_to='%Y/%m/%d/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title