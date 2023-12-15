from django.db import models
import os
from django.utils import timezone

def berkas_path(instance, filename):
    # Define the new filename here, for example, using the timestamp
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename, file_extension = os.path.splitext(filename)
    new_filename = f"file_{timestamp}{file_extension}"

    # Return the full path for the file
    return os.path.join('berkas/', new_filename)

class Berkas(models.Model):
    file = models.FileField(upload_to=berkas_path, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'berkas'
