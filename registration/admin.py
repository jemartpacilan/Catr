from django.contrib import admin
from .models import Caterer, Consumer, Menu, Item, Image, Transaction, Package
# Register your models here.


class CatererAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['profile_image']}),
        (None, {'fields': ['user']}),
        (None, {'fields': ['first_name']}),
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['business_name']}),
        (None, {'fields': ['business_description']}),
        (None, {'fields': ['province_address']}),
        (None, {'fields': ['municipality_address']}),
        (None, {'fields': ['street_address']}),
        (None, {'fields': ['zip_code']}),
        (None, {'fields': ['user_type']}),
    ]


class ConsumerAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['profile_image']}),
        (None, {'fields': ['user']}),
        (None, {'fields': ['first_name']}),
        (None, {'fields': ['last_name']}),
        (None, {'fields': ['created_date']}),
        (None, {'fields': ['email']}),
        (None, {'fields': ['consumer_badge']}),
        (None, {'fields': ['history']}),
        (None, {'fields': ['user_type']}),
    ]


class PackageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['package_name']}),
        (None, {'fields': ['package_date_created']}),
        (None, {'fields': ['caterer']}),
    ]


class MenuAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['caterer']}),
        (None, {'fields': ['course']}),
        (None, {'fields': ['menu_date_added']}),
        (None, {'fields': ['package']}),
    ]


class ItemAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['menu']}),
        (None, {'fields': ['tray']}),
        (None, {'fields': ['item_quantity']})
    ]


class ImageAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['image_uploaded_date']}),
        (None, {'fields': ['image_binary']}),
        (None, {'fields': ['image_name']}),
        (None, {'fields': ['menu']}),
    ]


class TransactionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['history']}),
        (None, {'fields': ['tray']}),
        (None, {'fields': ['transaction_date']}),
        (None, {'fields': ['caterer']}),
    ]


admin.site.register(Transaction, TransactionAdmin)
admin.site.register(Caterer, CatererAdmin)
admin.site.register(Consumer, ConsumerAdmin)
admin.site.register(Menu, MenuAdmin)
admin.site.register(Item, ItemAdmin)
admin.site.register(Image, ImageAdmin)
admin.site.register(Package, PackageAdmin)