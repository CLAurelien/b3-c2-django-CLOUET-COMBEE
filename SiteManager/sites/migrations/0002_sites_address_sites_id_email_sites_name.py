# Generated by Django 5.0 on 2024-02-18 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sites',
            name='address',
            field=models.CharField(blank=True, max_length=100),
        ),
        migrations.AddField(
            model_name='sites',
            name='id_email',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='sites',
            name='name',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
