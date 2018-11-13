from django.db import models
from django.contrib.auth.models import User


class Events(models.Model):
    title = models.CharField(max_length = 128)
    description = models.TextField()
    date = models.DateTimeField()

    def __str__(self):
        return self.title

class Follow(models.Model):
    user_id = models.ForeignKey(User, on_delete = models.PROTECT)
    event_id = models.ForeignKey(Events, on_delete = models.CASCADE)
