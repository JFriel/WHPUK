from django.db import models

# Create your models here.
class addsong(models.Model):
	songtitle = models.CharField(max_length=30)
	