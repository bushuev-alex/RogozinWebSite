from django.db import models


class ChildPoetry(models.Model):
    title = models.TextField()
    text = models.TextField()
