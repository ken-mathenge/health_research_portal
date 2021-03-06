# Generated by Django 3.0.3 on 2020-03-22 11:32

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("researches", "0020_auto_20200322_1310"),
    ]

    operations = [
        migrations.RenameField(
            model_name="review",
            old_name="selected_checklist",
            new_name="checklist",
        ),
        migrations.RenameField(
            model_name="reviewchecklist",
            old_name="checklist",
            new_name="create_checklist",
        ),
        migrations.AlterField(
            model_name="recommends",
            name="recommends",
            field=models.ManyToManyField(
                blank=True,
                related_name="recommends",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AlterField(
            model_name="recommends",
            name="research",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="researches",
                to="researches.Research",
            ),
        ),
    ]
