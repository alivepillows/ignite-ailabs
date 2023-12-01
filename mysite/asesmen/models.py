from django.db import models

# Create your models here.
class Asesmen(models.Model):
    tgl_mulai = models.DateField(auto_now_add=True)
    tgl_akhir = models.DateField(auto_now=True)
    time_expired = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='profil_image/')

    class Meta:
        managed = False
        db_table = 'asesmen'

