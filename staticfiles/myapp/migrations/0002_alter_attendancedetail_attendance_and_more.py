# Generated by Django 4.2.5 on 2023-09-27 13:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendancedetail',
            name='attendance',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='attendancedetail',
            name='employee',
            field=models.CharField(max_length=100),
        ),
    ]
