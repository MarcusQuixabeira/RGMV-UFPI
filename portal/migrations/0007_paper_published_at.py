# Generated by Django 2.2.4 on 2019-08-16 13:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_auto_20190816_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='paper',
            name='published_at',
            field=models.DateField(blank=True, null=True),
        ),
    ]