# Generated by Django 5.1.4 on 2025-01-13 13:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DKBTransaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('booking_date', models.DateTimeField()),
                ('value_date', models.DateTimeField()),
                ('sender', models.CharField(max_length=128)),
                ('receiver', models.CharField(max_length=128)),
                ('status', models.CharField(max_length=128)),
                ('payment_type', models.CharField(max_length=64)),
                ('iban', models.CharField(max_length=64)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TransactionFileUpload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('processed', models.BooleanField(default=False)),
                ('original_csv', models.FileField(upload_to='banking/csv/')),
                ('file_name', models.CharField(max_length=64, unique=True)),
            ],
        ),
    ]
