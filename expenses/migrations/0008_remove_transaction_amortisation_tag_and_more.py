# Generated by Django 4.1.2 on 2022-10-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0007_amortisationtarget_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transaction',
            name='amortisation_tag',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='participant',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
