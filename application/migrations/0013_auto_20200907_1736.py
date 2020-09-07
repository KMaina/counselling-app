# Generated by Django 3.1 on 2020-09-07 14:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0012_discussion_comment'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='discussion',
            name='comment',
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('discussion', models.ManyToManyField(to='application.Discussion')),
            ],
        ),
    ]
