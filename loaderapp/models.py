from django.db import models
from django.contrib import admin


class Brand(models.Model):
    key = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)


class CategoryTree(models.Model):
    key = models.CharField(max_length=64, unique=True)
    name = models.CharField(max_length=64)


class BrandThreshold(models.Model):
    version = models.CharField(max_length=12)
    brand = models.ForeignKey(Brand, to_field="key", on_delete=models.CASCADE)
    min_threshold = models.DecimalField(max_digits=17, decimal_places=16)


class Item(models.Model):
    item_key = models.CharField(max_length=64, help_text="GTIN/RIN/RSD", null=True, blank=True)
    brand = models.ForeignKey(Brand, to_field='key', null=True, on_delete=models.PROTECT)
    category = models.ForeignKey(CategoryTree, to_field="key", null=True, on_delete=models.PROTECT)
    banner = models.CharField(max_length=64, null=True)
    namespace = models.CharField(max_length=64, null=True)
