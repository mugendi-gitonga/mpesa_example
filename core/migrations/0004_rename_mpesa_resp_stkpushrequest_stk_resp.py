# Generated by Django 5.1.2 on 2024-11-04 09:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_rename_resp_stkpushrequest_mpesa_resp'),
    ]

    operations = [
        migrations.RenameField(
            model_name='stkpushrequest',
            old_name='mpesa_resp',
            new_name='stk_resp',
        ),
    ]
