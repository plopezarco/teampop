# Generated by Django 3.2.8 on 2021-11-17 09:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('baloOkindegia', '0008_delete_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bezeroa',
            name='abizena',
        ),
        migrations.RemoveField(
            model_name='bezeroa',
            name='email',
        ),
        migrations.RemoveField(
            model_name='bezeroa',
            name='izena',
        ),
        migrations.AddField(
            model_name='bezeroa',
            name='irudia',
            field=models.TextField(default=''),
        ),
    ]
