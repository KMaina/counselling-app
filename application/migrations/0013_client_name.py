# Generated by Django 3.1 on 2020-09-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_client_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='name',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
