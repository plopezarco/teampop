# Generated by Django 3.2.8 on 2021-10-22 08:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Banatzailea',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nan', models.CharField(max_length=9)),
                ('izena', models.CharField(max_length=50)),
                ('abizena', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefonoa', models.CharField(max_length=9)),
                ('libre_dago', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Bezeroa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=50)),
                ('abizena', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('telefonoa', models.CharField(max_length=9)),
                ('erabiltzailea', models.CharField(max_length=50)),
                ('pasahitza', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Produktua',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('izena', models.CharField(max_length=50)),
                ('prezioa', models.FloatField()),
                ('irudia', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_ticket', models.CharField(max_length=50)),
                ('data', models.DateField()),
                ('totala', models.FloatField()),
                ('id_banatzailea', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baloOkindegia.banatzailea')),
                ('id_bezeroa', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baloOkindegia.bezeroa')),
            ],
        ),
        migrations.CreateModel(
            name='Ticket_Lerroa',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('kantitatea', models.FloatField()),
                ('subtotala', models.FloatField()),
                ('id_produktua', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baloOkindegia.produktua')),
                ('id_ticket', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='baloOkindegia.ticket')),
            ],
        ),
    ]
