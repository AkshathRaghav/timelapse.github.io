# Generated by Django 3.1.7 on 2021-04-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_auto_20210312_1840'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='discord_id',
            field=models.CharField(default=0, max_length=100),
            preserve_default=False,
        ),
    ]
