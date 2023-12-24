# Generated by Django 4.2.7 on 2023-12-24 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bintang', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'rating',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.CharField(blank=True, max_length=255, null=True)),
                ('image', models.CharField(blank=True, max_length=255, null=True)),
                ('nik_ts', models.IntegerField(blank=True, null=True)),
                ('unit_bisnis', models.CharField(blank=True, max_length=255, null=True)),
                ('point', models.IntegerField(blank=True, null=True)),
                ('course_id', models.IntegerField(blank=True, null=True)),
                ('role', models.TextField(blank=True, null=True)),
                ('password', models.CharField(blank=True, max_length=255, null=True)),
                ('phone_number', models.CharField(blank=True, max_length=15, null=True)),
                ('username', models.CharField(blank=True, max_length=20, null=True)),
                ('first_name', models.CharField(blank=True, max_length=255, null=True)),
                ('last_name', models.CharField(blank=True, max_length=255, null=True)),
                ('created_at', models.DateTimeField(blank=True, null=True)),
                ('update_at', models.DateTimeField(blank=True, null=True)),
            ],
            options={
                'db_table': 'user',
                'managed': False,
            },
        ),
    ]
