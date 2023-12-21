from django.db import models
import os
from django.utils import timezone

def course_image_path(instance, filename):
    # Define the new filename here, for example, using the timestamp
    timestamp = timezone.now().strftime('%Y%m%d%H%M%S')
    filename, file_extension = os.path.splitext(filename)
    new_filename = f"course_{timestamp}{file_extension}"

    # Return the full path for the file
    return os.path.join('course_image/', new_filename)

class User(models.Model):
    email = models.CharField(max_length=255, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    nik_ts = models.IntegerField(blank=True, null=True)
    unit_bisnis = models.CharField(max_length=255, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    course_id = models.IntegerField(blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)
    first_name = models.CharField(max_length=255, blank=True, null=True)
    last_name = models.CharField(max_length=255, blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    update_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'

class Rating(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    bintang = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'rating'

class Benefit(models.Model):
    deskripsi = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'benefit'

class Jawaban(models.Model):
    jawaban = models.CharField(max_length=255, blank=True, null=True)
    jenis = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'jawaban'

class Quiz(models.Model):
    image = models.CharField(max_length=255, blank=True, null=True)
    title = models.CharField(max_length=255, blank=True, null=True)
    soal = models.CharField(max_length=255, blank=True, null=True)
    jawaban = models.ForeignKey(Jawaban, models.DO_NOTHING, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    nilai = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'quiz'


class Berkas(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'berkas'


class SubCourse(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, models.DO_NOTHING, blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    berkas = models.ForeignKey(Berkas, models.DO_NOTHING, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_course'

class Course(models.Model):
    image = models.ImageField(upload_to = course_image_path, blank=True, null=True)
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    subcourse = models.ForeignKey('SubCourse', models.DO_NOTHING, blank=True, null=True)
    rating = models.ForeignKey('Rating', models.DO_NOTHING, blank=True, null=True)
    level = models.TextField(blank=True, null=True)  # This field type is a guess.
    benefit = models.ForeignKey(Benefit, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'