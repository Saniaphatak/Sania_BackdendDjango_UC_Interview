from django.db import models
class Pokemon(models.Model):
    name = models.CharField(max_length=50)
    image = models.URLField()
    pokemon_type = models.CharField(max_length=50)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
     return self.name
