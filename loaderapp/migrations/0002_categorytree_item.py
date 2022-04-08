# Generated by Django 2.2 on 2022-04-08 19:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('loaderapp', '0001_brand_brandthreshold'),
    ]

    operations = [
        migrations.CreateModel(
            name='CategoryTree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('key', models.CharField(max_length=64, unique=True)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_key', models.CharField(blank=True, help_text='GTIN/RIN/RSD', max_length=64, null=True)),
                ('banner', models.CharField(max_length=64, null=True)),
                ('namespace', models.CharField(max_length=64, null=True)),
                ('brand', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loaderapp.Brand', to_field='key')),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='loaderapp.CategoryTree', to_field='key')),
            ],
        ),
    ]