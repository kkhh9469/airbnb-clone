# Generated by Django 3.1.1 on 2020-09-30 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0011_auto_20200912_2214'),
    ]

    operations = [
        migrations.AlterField(
            model_name='room',
            name='guests',
            field=models.IntegerField(help_text='How many people will be staying?'),
        ),
    ]
