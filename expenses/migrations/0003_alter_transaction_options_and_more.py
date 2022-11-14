# Generated by Django 4.1.2 on 2022-10-31 11:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0002_alter_transaction_direction'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transaction',
            options={'ordering': ['-date']},
        ),
        migrations.AddField(
            model_name='transaction',
            name='amortisation_tag',
            field=models.CharField(default='', max_length=32),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('A', 'Allowance'), ('M', 'Amortisation'), ('F', 'Food'), ('L', 'Leisure'), ('O', 'Offer'), ('T', 'Transport'), ('_', 'Other')], max_length=1),
        ),
    ]
