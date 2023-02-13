from django.db import models

class Catgeory(models.Model):
    simple = models.CharField(max_length=255)

class Watch(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.ForeignKey(Catgeory, on_delete=models.CASCADE,
                                 null=True)
