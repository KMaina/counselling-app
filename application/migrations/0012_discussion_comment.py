# Generated by Django 3.1 on 2020-09-07 10:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20200903_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='discussion',
            name='comment',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
