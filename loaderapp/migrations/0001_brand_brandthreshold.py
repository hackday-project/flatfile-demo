# Generated by Django 2.0 on 2022-04-06 18:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='BrandThreshold',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.CharField(max_length=12)),
                ('min_threshold', models.DecimalField(decimal_places=16, max_digits=17)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='loaderapp.Brand', to_field='key')),
            ],
        ),
    ]
