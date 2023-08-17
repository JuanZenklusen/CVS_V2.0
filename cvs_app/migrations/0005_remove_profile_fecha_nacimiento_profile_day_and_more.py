# Generated by Django 4.2.4 on 2023-08-12 20:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs_app', '0004_alter_profile_genero'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='profile',
            name='fecha_nacimiento',
        ),
        migrations.AddField(
            model_name='profile',
            name='day',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='month',
            field=models.IntegerField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='year',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]