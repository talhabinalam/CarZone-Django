from typing import Any
from django.db import models


class Team(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=50)
    photo = models.ImageField(upload_to='photos/team_profile')
    facebook_link = models.URLField(max_length=150)
    twitter_link = models.URLField(max_length=150)
    google_plus_link = models.URLField(max_length=150)
    created_date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.first_name