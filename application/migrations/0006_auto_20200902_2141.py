# Generated by Django 3.1 on 2020-09-02 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0005_client_issue'),
    ]

    operations = [
        migrations.AlterField(
            model_name='counsellor',
            name='profile_photo',
            field=models.ImageField(default='default.png', upload_to='profile_pics'),
        ),
    ]
