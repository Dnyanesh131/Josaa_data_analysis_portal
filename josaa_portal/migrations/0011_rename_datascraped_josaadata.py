# Generated by Django 4.2.2 on 2023-07-04 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('josaa_portal', '0010_alter_datascraped_academic'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Datascraped',
            new_name='JosaaData',
        ),
    ]
