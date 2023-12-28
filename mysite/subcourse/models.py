from django.db import models

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=255)
    birth_date = models.DateField(db_column='birth__date')  # Field renamed because it contained more than one '_' in a row.
    address = models.CharField(max_length=50)
    nik = models.IntegerField()
    unit = models.CharField(max_length=50)
    role = models.TextField()  # This field type is a guess.
    image = models.CharField(max_length=225, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'user'


class Berkas(models.Model):
    file = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'berkas'


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


class Course(models.Model):
    id_course = models.AutoField(primary_key=True)
    theme_course = models.CharField(max_length=100, blank=True, null=True)
    cover = models.CharField(max_length=100, blank=True, null=True)
    level = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    description = models.CharField(max_length=200, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'course'
        

class SubCourse(models.Model):
    id_sub_course = models.AutoField(primary_key=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_course'