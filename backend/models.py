from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=400)
    username = models.CharField(max_length=300, default="Unknown")

    def __str__(self):
        return self.title + ' ' + self.text
