# Generated by Django 3.2.3 on 2022-03-01 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0022_alter_frontend_order_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frontend_order',
            name='USer',
            field=models.CharField(max_length=50, null=True),
        ),
    ]
