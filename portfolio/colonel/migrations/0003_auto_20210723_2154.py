# Generated by Django 3.2.5 on 2021-07-23 16:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('colonel', '0002_gallery'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='gallery',
            name='title',
        ),
        migrations.AlterField(
            model_name='about',
            name='career',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='heading',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='gallery',
            name='image',
            field=models.ImageField(upload_to='gallery/'),
        ),
        migrations.AlterField(
            model_name='home',
            name='greeting2',
            field=models.CharField(max_length=15),
        ),
        migrations.AlterField(
            model_name='skills',
            name='skill_name',
            field=models.CharField(max_length=50),
        ),
    ]
