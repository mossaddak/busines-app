# Generated by Django 3.2.3 on 2022-03-25 18:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('business_app', '0071_remove_frontend_rating_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend_rating',
            name='USer',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
