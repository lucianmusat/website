from django.db import models

class About(models.Model):
    content = models.TextField()