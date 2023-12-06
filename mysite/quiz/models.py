from django.db import models

# Create your models here.

    
class Jawaban(models.Model):
    jawaban = models.CharField(max_length=255, blank=True, null=True)
    jenis = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jawaban'

class Quiz(models.Model):
    image = models.ImageField(upload_to='image_quiz/', blank=True, null=True)
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
