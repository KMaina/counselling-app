# Generated by Django 3.1 on 2020-09-06 02:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_auto_20200903_1115'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='profile_photo',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
