# Generated by Django 4.1.2 on 2022-10-31 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0003_alter_transaction_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('A', 'Allowance'), ('F', 'Food'), ('L', 'Leisure'), ('O', 'Offer'), ('T', 'Transport'), ('_', 'Other')], max_length=1),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='method',
            field=models.CharField(choices=[('A', 'Amortisation'), ('B', 'Bacs'), ('C', 'Card'), ('S', 'Cash'), ('Q', 'Cheque'), ('P', 'PayPal')], max_length=1),
        ),
    ]
