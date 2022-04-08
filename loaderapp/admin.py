from django.contrib import admin
from loaderapp.models import Brand, BrandThreshold, Item
# Register your models here.


@admin.register(BrandThreshold)
class BrandThresholdAdmin(admin.ModelAdmin):
    list_display = ('version', 'view_brand', 'min_threshold')

    def view_brand(self, obj):
        return obj.brand.key


@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('key', 'name')

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('item_key', 'brand', 'category', 'namespace', 'banner')