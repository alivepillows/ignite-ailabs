# Generated by Django 4.2.7 on 2023-12-24 05:22

import berkas.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Berkas',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file', models.FileField(blank=True, null=True, upload_to=berkas.models.berkas_path)),
            ],
            options={
                'db_table': 'berkas',
                'managed': False,
            },
        ),
    ]
