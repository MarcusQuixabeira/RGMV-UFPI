# Generated by Django 2.2.4 on 2019-08-15 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0003_auto_20190815_0117'),
    ]

    operations = [
        migrations.AddField(
            model_name='researcher',
            name='ensino',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
    ]
