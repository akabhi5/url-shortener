from django.db import models

class Links(models.Model):
    new_url = models.TextField()
    original_url = models.TextField()

    def __str__(self):
        return self.new_url