# Generated by Django 3.1.7 on 2021-04-26 18:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0013_auto_20210426_2339'),
    ]

    operations = [
        migrations.AlterField(
            model_name='events',
            name='grade',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='events',
            name='number',
            field=models.CharField(default='Not Added Yet', max_length=20),
        ),
        migrations.AlterField(
            model_name='events',
            name='schoolname',
            field=models.CharField(default='Not Added Yet', max_length=150),
        ),
        migrations.AlterField(
            model_name='events',
            name='section',
            field=models.CharField(default='*', max_length=5),
        ),
    ]
