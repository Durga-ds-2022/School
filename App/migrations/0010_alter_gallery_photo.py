# Generated by Django 4.2.3 on 2023-09-03 16:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0009_alter_gallery_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='gallery',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='Gallery'),
        ),
    ]