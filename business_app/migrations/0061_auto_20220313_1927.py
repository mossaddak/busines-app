# Generated by Django 3.2.3 on 2022-03-13 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0060_auto_20220313_1921'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backend_order',
            name='order_message',
        ),
        migrations.RemoveField(
            model_name='complete_website_orders',
            name='order_message',
        ),
    ]