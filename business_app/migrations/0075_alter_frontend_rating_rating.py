# Generated by Django 3.2.3 on 2022-03-26 11:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0074_alter_frontend_rating_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend_rating',
            name='Rating',
            field=models.IntegerField(null=True),
        ),
    ]
