# Generated by Django 4.1.2 on 2022-10-31 11:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expenses', '0005_alter_transaction_participant'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmortisationTarget',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=32)),
                ('target', models.IntegerField()),
            ],
        ),
    ]
