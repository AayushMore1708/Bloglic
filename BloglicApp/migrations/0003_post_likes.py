# Generated by Django 5.0.8 on 2024-08-07 17:12

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BloglicApp', '0002_comment'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='likes',
            field=models.ManyToManyField(related_name='post_likes', to=settings.AUTH_USER_MODEL),
        ),
    ]
