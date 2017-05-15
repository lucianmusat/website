from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(auto_now_add=True)
    body = models.TextField()
    slug = models.SlugField(max_length=40, unique=True)

    def __str__(self):
        return self.title

    def just_date(self):
        return self.date.date()

    def summary(self):
        body = self.body[:1000]
        if len(self.body) > 1000:
            body += "..."
        return body