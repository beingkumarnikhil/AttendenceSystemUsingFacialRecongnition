# Generated by Django 3.1.2 on 2020-11-28 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0006_attendance_img'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='img',
            field=models.FileField(null=True, upload_to='pics'),
        ),
    ]