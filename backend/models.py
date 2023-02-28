from django.db import models

class Question(models.Model):
    title = models.CharField(max_length=300)
    text = models.CharField(max_length=400)

    def __str__(self):
        return self.title + ' ' + self.text
        