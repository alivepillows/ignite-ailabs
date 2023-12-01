from django.db import models

# Create your models here.

class Asesmen(models.Model):
    tgl_mulai = models.DateField(blank=True, null=True)
    tgl_akhir = models.DateField(blank=True, null=True)
    time_expired = models.DateTimeField(blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asesmen'

class SubAsesmen(models.Model):
    pertanyaan = models.CharField(max_length=255, blank=True, null=True)
    nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_asesmen'

class PivotAsesmen(models.Model):
    asesmen = models.ForeignKey(Asesmen, models.DO_NOTHING, blank=True, null=True)
    sub_asesmen = models.ForeignKey(SubAsesmen, models.DO_NOTHING, blank=True, null=True)
    total_nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_asesmen'