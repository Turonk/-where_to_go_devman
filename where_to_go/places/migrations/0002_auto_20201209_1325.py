# Generated by Django 3.0.5 on 2020-12-09 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('places', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='place',
            name='lnп',
        ),
        migrations.AddField(
            model_name='place',
            name='lng',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
