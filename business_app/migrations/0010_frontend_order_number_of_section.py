# Generated by Django 3.2.3 on 2022-01-11 19:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0009_rename_file_system_frontend_order'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend_order',
            name='Number_of_Section',
            field=models.CharField(max_length=250, null=True),
        ),
    ]