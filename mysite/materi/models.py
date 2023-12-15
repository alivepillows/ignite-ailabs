from django.db import models
import os
from django.utils import timezone

def user_materi_path(instance, filename):
    # Define the new filename here, for example, using the timestamp
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename, file_extension = os.path.splitext(filename)
    new_filename = f"materi_{timestamp}{file_extension}"

    # Return the full path for the file
    return os.path.join('video_materi/', new_filename)

class Materi(models.Model):
    judul = models.CharField(max_length=255, blank=True, null=True)
    video = models.FileField(upload_to=user_materi_path, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'materi'