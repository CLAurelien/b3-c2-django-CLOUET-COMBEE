# Generated by Django 5.0.2 on 2024-02-18 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sites', '0002_sites_address_sites_id_email_sites_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sites',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]