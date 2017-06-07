from django.db import models
from tinymce import models as tinymce_models

class Index(models.Model):
    content = tinymce_models.HTMLField()

