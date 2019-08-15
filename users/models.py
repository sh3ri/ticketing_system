from PIL import Image
from django.contrib.auth.models import User
from django.db import models
from jsonfield import JSONField
import collections


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.png', upload_to='profile_pics')
    tickets = JSONField(default=[])

    def __str__(self):
        return f'{self.user.username} {self.image.__str__()} Profile'

    def save(self, *args, **kwargs):
        super().save()
        img = Image.open(self.image.path)
        if img.width > 128 or img.height > 128:
            new_size_tuple = (128, 128)
            img.thumbnail(new_size_tuple)
            img.save(self.image.path)
