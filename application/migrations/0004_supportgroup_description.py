# Generated by Django 3.1 on 2020-09-02 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0003_supportgroup_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='supportgroup',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
