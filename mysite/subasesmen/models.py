from django.db import models

class SubAsesmen(models.Model):
    pertanyaan = models.CharField(max_length=255, blank=False, null=False)
    nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_asesmen'



