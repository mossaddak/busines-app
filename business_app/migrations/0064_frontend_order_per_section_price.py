# Generated by Django 3.2.3 on 2022-03-16 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0063_backend_order_per_section_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='frontend_order',
            name='Per_section_Price',
            field=models.CharField(max_length=250, null=True),
        ),
    ]
