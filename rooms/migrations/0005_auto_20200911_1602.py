# Generated by Django 3.1.1 on 2020-09-11 07:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0004_auto_20200910_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='room',
            old_name='discription',
            new_name='description',
        ),
    ]
