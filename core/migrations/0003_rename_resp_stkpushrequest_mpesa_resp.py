# Generated by Django 5.1.2 on 2024-11-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_stkpushrequest'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stkpushrequest',
            old_name='resp',
            new_name='mpesa_resp',
        ),
    ]
