# Generated by Django 3.2.3 on 2021-12-28 19:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacts',
            name='text',
            field=models.TextField(null=True),
        ),
    ]