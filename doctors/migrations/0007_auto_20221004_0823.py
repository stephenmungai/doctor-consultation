# Generated by Django 3.2 on 2022-10-04 08:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0006_alter_doctor_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='consultation',
            name='diagnosis',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='consultation',
            name='remarks',
            field=models.TextField(blank=True, null=True),
        ),
    ]
