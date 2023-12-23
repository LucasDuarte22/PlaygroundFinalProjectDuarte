# Generated by Django 4.2.7 on 2023-12-18 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Almacenamiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='MemoriasRAM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Motherboards',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='PlacasDeVideo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Procesadores',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marca', models.CharField(max_length=50)),
                ('modelo', models.CharField(max_length=50)),
                ('anio', models.IntegerField()),
                ('descripcion', models.CharField(max_length=255)),
                ('precio', models.IntegerField()),
            ],
        ),
    ]
