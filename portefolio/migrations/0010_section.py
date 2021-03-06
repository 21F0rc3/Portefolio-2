# Generated by Django 4.0.5 on 2022-06-20 22:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0009_alter_project_logo_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('content_file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portefolio.file')),
                ('image_file', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portefolio.image')),
                ('project', models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portefolio.project')),
            ],
        ),
    ]
