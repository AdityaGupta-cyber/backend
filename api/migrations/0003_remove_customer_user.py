# Generated by Django 5.0.6 on 2024-07-15 19:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_customer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
    ]
