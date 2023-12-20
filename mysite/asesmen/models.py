from django.db import models
import os
from django.utils import timezone

# Create your models here.
def asesmen_image_path(instance, filename):
    # Define the new filename here, for example, using the timestamp
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename, file_extension = os.path.splitext(filename)
    new_filename = f"asesmen_{timestamp}{file_extension}"

    # Return the full path for the file
    return os.path.join('asesmen_image/', new_filename)


class Asesmen(models.Model):
    tgl_mulai = models.DateField(blank=True, null=True)
    tgl_akhir = models.DateField(blank=True, null=True)
    time_expired = models.DateTimeField(blank=True, null=True)
    image = models.ImageField(upload_to= asesmen_image_path, blank=True, null=True)
    sub_asesmen = models.ForeignKey('SubAsesmen', models.DO_NOTHING, blank=True, null=True)
    title = models.CharField(max_length=200, blank=True, null=True)


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
    
    def save(self, *args, **kwargs):
        # Calculate total_nilai here before saving
        if self.sub_asesmen and self.sub_asesmen.nilai:
            self.total_nilai = self.sub_asesmen.nilai  # You can modify this calculation as needed

        super(PivotAsesmen, self).save(*args, **kwargs)