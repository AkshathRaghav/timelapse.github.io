# Generated by Django 3.1.7 on 2021-04-26 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20210426_2337'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='number',
            field=models.CharField(max_length=20),
        ),
    ]
