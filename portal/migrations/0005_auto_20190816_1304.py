# Generated by Django 2.2.4 on 2019-08-16 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0004_researcher_ensino'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='abstract',
        ),
        migrations.RemoveField(
            model_name='article',
            name='first_author',
        ),
        migrations.RemoveField(
            model_name='article',
            name='researcher',
        ),
        migrations.AddField(
            model_name='article',
            name='paper',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='article',
            name='year',
            field=models.CharField(default='', max_length=4),
            preserve_default=False,
        ),
    ]
