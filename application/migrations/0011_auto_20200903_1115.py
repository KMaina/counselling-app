# Generated by Django 3.1 on 2020-09-03 08:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_auto_20200903_1101'),
    ]

    operations = [
        migrations.AlterField(
            model_name='discussion',
            name='sender',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='application.client'),
        ),
    ]
