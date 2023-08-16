from django.db import models

class BaseMode(models.Model):
    created_at = models.CharField()