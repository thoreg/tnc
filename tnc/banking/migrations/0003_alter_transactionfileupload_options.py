# Generated by Django 5.1.4 on 2025-01-15 07:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("banking", "0002_alter_dkbtransaction_options_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="transactionfileupload",
            options={"managed": False},
        ),
    ]
