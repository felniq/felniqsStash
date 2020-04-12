from django.db import models

# Create your models here.


class AvailableImages(models.Model):
    image_path = models.CharField(max_length=300)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.image_path
