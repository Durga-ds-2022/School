# Generated by Django 4.2.3 on 2023-08-14 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0005_alter_testimonial_message'),
    ]

    operations = [
        migrations.AddField(
            model_name='announcements',
            name='is_display',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='announcements',
            name='news',
            field=models.CharField(default='Na', max_length=500),
        ),
    ]
