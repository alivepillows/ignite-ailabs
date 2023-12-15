from django.db import models

# Create your models here.

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

class Berkas(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'berkas'

class SubCourse(models.Model):
    user = models.ForeignKey('User', models.DO_NOTHING, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    subcourse = models.CharField(max_length=255, blank=True, null=True)
    quiz_id = models.IntegerField(blank=True, null=True)
    judul = models.CharField(max_length=255, blank=True, null=True)
    berkas = models.ForeignKey(Berkas, models.DO_NOTHING, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_course'