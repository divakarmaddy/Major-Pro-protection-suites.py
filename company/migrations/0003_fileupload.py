# Generated by Django 4.0 on 2023-11-10 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0002_register_status'),
    ]

    operations = [
        migrations.CreateModel(
            name='fileupload',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('Mail', models.CharField(max_length=20)),
                ('Designation', models.CharField(max_length=20)),
                ('Picture', models.FileField(upload_to='')),
            ],
        ),
    ]
