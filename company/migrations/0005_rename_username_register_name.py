# Generated by Django 4.0 on 2023-12-01 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_rename_name_register_username'),
    ]

    operations = [
        migrations.RenameField(
            model_name='register',
            old_name='UserName',
            new_name='Name',
        ),
    ]
