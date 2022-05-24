# Generated by Django 3.2.3 on 2022-03-12 18:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0046_auto_20220309_0251'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frontend_order',
            name='order_message',
        ),
        migrations.AddField(
            model_name='frontend_order',
            name='order_message',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='all_notifications', to='business_app.message_manu'),
        ),
    ]
