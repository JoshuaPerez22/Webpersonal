# Generated by Django 4.1.5 on 2023-01-07 00:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0003_alter_project_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='description',
            field=models.TextField(default=False),
            preserve_default=False,
        ),
    ]
