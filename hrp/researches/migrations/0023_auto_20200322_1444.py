# Generated by Django 3.0.3 on 2020-03-22 11:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('researches', '0022_auto_20200322_1434'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recommends',
            name='recommends',
        ),
        migrations.AddField(
            model_name='recommends',
            name='recommends',
            field=models.ManyToManyField(blank=True, related_name='recommends', to=settings.AUTH_USER_MODEL),
        ),
    ]
