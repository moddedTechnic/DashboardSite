# Generated by Django 4.1.2 on 2022-11-03 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0012_alter_transaction_amortisation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='participant',
            field=models.CharField(blank=True, max_length=64, null=True),
        ),
    ]
