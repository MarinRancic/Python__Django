# Generated by Django 4.0.5 on 2022-06-14 22:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_upis'),
    ]

    operations = [
        migrations.AddField(
            model_name='predmeti',
            name='nositelj_predmeta',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
