# Generated by Django 3.2 on 2022-10-09 10:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('patients', '0006_ticketmedia'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticketmedia',
            name='caption',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='ticketmedia',
            name='file',
            field=models.FileField(upload_to='media'),
        ),
    ]
