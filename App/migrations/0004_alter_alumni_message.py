# Generated by Django 4.2.3 on 2023-08-14 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0003_rename_is_vedio_display_event_is_video_display_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alumni',
            name='message',
            field=models.CharField(max_length=500),
        ),
    ]
