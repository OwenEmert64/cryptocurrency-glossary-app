from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"

class Term(models.Model):
    term = models.CharField(max_length=100)
    definition = models.TextField()
    category = models.CharField(max_length=50, blank=True)
    added_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    favorited_by = models.ManyToManyField(User, related_name='favorites', blank=True)
    def __str__(self):
        return self.term
