# Generated by Django 4.1.5 on 2023-01-09 01:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_project_url_alter_project_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='url',
            new_name='link',
        ),
    ]
