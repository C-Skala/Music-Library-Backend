# Generated by Django 4.1 on 2022-08-25 02:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('music_library_backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Product',
            new_name='Song',
        ),
    ]
