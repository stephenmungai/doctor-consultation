# Generated by Django 3.2 on 2022-10-09 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0007_auto_20221009_1016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ticketmedia',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]