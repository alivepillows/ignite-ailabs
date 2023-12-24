# Generated by Django 4.2.7 on 2023-12-24 05:22

from django.db import migrations, models
import quiz.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jawaban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jawaban', models.CharField(blank=True, max_length=255, null=True)),
                ('jenis', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'jawaban',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='PivotJawaban',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_nilai', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'pivot_jawaban',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to=quiz.models.quiz_image_path)),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('soal', models.CharField(blank=True, max_length=255, null=True)),
                ('status', models.TextField(blank=True, null=True)),
                ('nilai', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'quiz',
                'managed': False,
            },
        ),
    ]
