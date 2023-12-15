from django.db import models

# Create your models here.
class Benefit(models.Model):
    deskripsi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'benefit'