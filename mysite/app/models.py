from django.db import models

# Create your models here.

# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Asesmen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    judul_asesmen = models.CharField(max_length=255, blank=True, null=True)
    tgl_awal_pengisian = models.DateField(blank=True, null=True)
    tgl_akhir_pengisian = models.DateField(blank=True, null=True)
    time_expired = models.TimeField(blank=True, null=True)
    sub_asesmen = models.ForeignKey('SubAsesmen', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'asesmen'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Course(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kode_kelas = models.IntegerField(blank=True, null=True)
    gambar = models.CharField(max_length=255, blank=True, null=True)
    deskripsi = models.TextField(blank=True, null=True)
    level = models.IntegerField(blank=True, null=True)
    progress = models.IntegerField(blank=True, null=True)
    sub_course = models.ForeignKey('SubCourse', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'course'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Ide(models.Model):
    id = models.BigIntegerField(primary_key=True)
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.IntegerField(blank=True, null=True)
    problem = models.CharField(max_length=255, blank=True, null=True)
    solution = models.CharField(max_length=255, blank=True, null=True)
    user_segment = models.CharField(max_length=255, blank=True, null=True)
    unique_value = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'ide'


class Quiz(models.Model):
    id = models.BigIntegerField(primary_key=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    kode_quiz = models.IntegerField(blank=True, null=True)
    skor_minimum = models.IntegerField(blank=True, null=True)
    jumlah_soal = models.IntegerField(blank=True, null=True)
    nilai = models.IntegerField(blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'quiz'


class SubAsesmen(models.Model):
    id = models.BigIntegerField(primary_key=True)
    asesmen_pernyataan = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_asesmen'


class SubCourse(models.Model):
    id = models.BigIntegerField(primary_key=True)
    kode_materi = models.IntegerField(blank=True, null=True)
    judul_materi = models.CharField(max_length=255, blank=True, null=True)
    jenis_konten = models.CharField(max_length=20, blank=True, null=True)
    konten = models.CharField(max_length=255, blank=True, null=True)
    durasi_menit_belajar = models.TimeField(blank=True, null=True)
    quiz = models.ForeignKey(Quiz, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'sub_course'


class User(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    image = models.ImageField(upload_to='profile_image/', null=True, blank=True)
    nik_ts = models.IntegerField(blank=True, null=True)
    unit_bisnis = models.CharField(max_length=255, blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    course = models.ForeignKey(Course, models.DO_NOTHING, blank=True, null=True)
    role = models.TextField(blank=True, null=True)  # This field type is a guess.
    password = models.CharField(max_length=255, blank=True, null=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'