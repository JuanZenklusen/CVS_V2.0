# Generated by Django 4.2.4 on 2023-08-20 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cvs_app', '0015_alter_about_me_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about_me',
            name='aptitudes',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='habilidades',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AlterField(
            model_name='about_me',
            name='objetivo',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
