# Generated by Django 2.2.4 on 2019-08-14 23:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('abstract', models.TextField(max_length=800)),
                ('conservation', models.BooleanField()),
                ('breeding', models.BooleanField()),
                ('researcher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='portal.Researcher')),
            ],
        ),
    ]
