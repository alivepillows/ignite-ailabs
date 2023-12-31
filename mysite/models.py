# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Article(models.Model):
    id_article = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    link = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    id_materials = models.ForeignKey('Materials', models.DO_NOTHING, db_column='id_materials')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'article'


class Assesment(models.Model):
    id_assesment = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    deadline = models.DateField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'assesment'


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


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.OneToOneField(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class Benefit(models.Model):
    id_benefit = models.AutoField(primary_key=True)
    description = models.TextField(blank=True, null=True)
    id_course = models.ForeignKey('Course', models.DO_NOTHING, db_column='id_course')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'benefit'


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


class File(models.Model):
    id_file = models.AutoField(primary_key=True)
    fie_name = models.CharField(max_length=255, blank=True, null=True)
    id_materials = models.ForeignKey('Materials', models.DO_NOTHING, db_column='id_materials')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'file'


class Materials(models.Model):
    id_materials = models.AutoField(primary_key=True)
    theme_materials = models.CharField(max_length=100, blank=True, null=True)
    type = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_sub_course = models.ForeignKey('SubCourse', models.DO_NOTHING, db_column='id_sub_course')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'materials'


class Options(models.Model):
    id_options = models.AutoField(primary_key=True)
    options = models.CharField(max_length=100, blank=True, null=True)
    status = models.TextField(blank=True, null=True)  # This field type is a guess.
    id_question_materials = models.ForeignKey('QuestionMaterials', models.DO_NOTHING, db_column='id_question_materials')
    id_materials = models.ForeignKey(Materials, models.DO_NOTHING, db_column='id_materials')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'options'


class QuesAsessment(models.Model):
    id_ques_asessment = models.AutoField(primary_key=True)
    question = models.CharField(max_length=100, blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    id_sub_assesment = models.ForeignKey('SubAssesment', models.DO_NOTHING, db_column='id_sub_assesment')
    charakter = models.CharField(max_length=100, blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'ques_asessment'


class QuestionMaterials(models.Model):
    id_question_materials = models.AutoField(primary_key=True)
    question_quiz = models.CharField(max_length=255, blank=True, null=True)
    id_quiz = models.ForeignKey('Quiz', models.DO_NOTHING, db_column='id_quiz')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'question_materials'


class Quiz(models.Model):
    id_quiz = models.AutoField(primary_key=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    id_materials = models.ForeignKey(Materials, models.DO_NOTHING, db_column='id_materials')
    title = models.CharField(max_length=100, blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'quiz'


class Rating(models.Model):
    id_rating = models.AutoField(primary_key=True)
    id_user = models.ForeignKey('User', models.DO_NOTHING, db_column='id_user')
    range = models.FloatField(blank=True, null=True)
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'rating'


class SubAssesment(models.Model):
    id_sub_assesment = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    image = models.CharField(max_length=255, blank=True, null=True)
    question_asessment = models.CharField(max_length=100, blank=True, null=True)
    duration = models.TimeField(blank=True, null=True)
    id_assesment = models.ForeignKey(Assesment, models.DO_NOTHING, db_column='id_assesment')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_assesment'


class SubCourse(models.Model):
    id_sub_course = models.AutoField(primary_key=True)
    sub_title = models.CharField(max_length=100, blank=True, null=True)
    id_course = models.ForeignKey(Course, models.DO_NOTHING, db_column='id_course')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'sub_course'


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


class Video(models.Model):
    id_video = models.AutoField(primary_key=True)
    video_name = models.CharField(max_length=255, blank=True, null=True)
    id_materials = models.ForeignKey(Materials, models.DO_NOTHING, db_column='id_materials')
    createdat = models.DateTimeField(db_column='createdAt', blank=True, null=True)  # Field name made lowercase.
    updateat = models.DateTimeField(db_column='updateAt', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'video'
