from django.db import models
from django.contrib.postgres.fields import JSONField

class FavCharacter(models.Model):
    char_id = models.CharField(max_length=255, unique=False)
    char_key = models.CharField(max_length=255, unique=False)
    char_name = models.CharField(max_length=255, unique=True)
    json_data = JSONField()
    craeted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.char_name