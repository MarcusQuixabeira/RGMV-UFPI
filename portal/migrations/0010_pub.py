# Generated by Django 2.2.4 on 2019-08-16 14:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0009_delete_paper'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pub',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=4)),
                ('link', models.CharField(max_length=600)),
                ('paper', models.CharField(max_length=100)),
            ],
        ),
    ]
