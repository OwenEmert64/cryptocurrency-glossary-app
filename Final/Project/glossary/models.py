from django.db import models

class Term(models.Model):
    title = models.CharField(max_length=100)
    definition = models.TextField()

    def __str__(self):
        return self.title

