# Generated by Django 4.0.5 on 2022-06-20 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0003_rename_project_name_project_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=200, unique=True)),
            ],
        ),
    ]
