# Generated by Django 4.1.2 on 2022-10-31 11:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0009_transaction_amortisation_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='amortisation_tag',
            new_name='amortisation',
        ),
    ]
