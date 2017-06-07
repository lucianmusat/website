from django.db import models
from tinymce import models as tinymce_models

class About(models.Model):
    content = tinymce_models.HTMLField()