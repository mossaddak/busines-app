# Generated by Django 3.2.3 on 2022-05-10 20:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business_app', '0090_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='faq',
            name='Answer',
            field=models.TextField(blank=True, null=True),
        ),
    ]
