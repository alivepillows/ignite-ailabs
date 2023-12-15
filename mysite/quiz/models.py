from django.db import models
import os
from django.utils import timezone

def quiz_image_path(instance, filename):
    # Define the new filename here, for example, using the timestamp
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename, file_extension = os.path.splitext(filename)
    new_filename = f"quiz_{timestamp}{file_extension}"

    # Return the full path for the file
    return os.path.join('quiz_image/', new_filename)

    
class Jawaban(models.Model):
    jawaban = models.CharField(max_length=255, blank=True, null=True)
    jenis = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jawaban'

class Quiz(models.Model):
    image = models.ImageField(upload_to= quiz_image_path, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    soal = models.CharField(max_length=255, blank=True, null=True)
    jawaban = models.ForeignKey(Jawaban, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    nilai = models.IntegerField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'quiz'
        

class PivotJawaban(models.Model):
    quiz = models.ForeignKey('Quiz', models.DO_NOTHING, blank=True, null=True)
    jawaban = models.ForeignKey(Jawaban, models.DO_NOTHING, blank=True, null=True)
    total_nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'pivot_jawaban'
