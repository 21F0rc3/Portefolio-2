# Generated by Django 4.0.5 on 2022-06-20 15:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portefolio', '0008_alter_project_logo_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='logo_image',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='portefolio.image'),
        ),
    ]
