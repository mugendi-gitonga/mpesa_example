# Generated by Django 5.1.2 on 2024-11-04 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='MpesaDepositTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(max_length=15)),
                ('acc_number', models.CharField(max_length=15)),
                ('names', models.CharField(max_length=50)),
                ('transaction_id', models.CharField(max_length=20, unique=True)),
                ('amount', models.IntegerField()),
                ('trans_date', models.DateTimeField()),
                ('status', models.CharField(choices=[('PENDING', 'PENDING'), ('VALIDATING', 'VALIDATING'), ('SUCCESS', 'SUCCESS'), ('FAILED', 'FAILED')], default='PENDING', max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
        ),
    ]
