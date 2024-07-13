from django.contrib import admin

from onlineshop.models import Product, SalesNetwork


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):

    list_display = ('name', 'model', 'release_date')


@admin.register(SalesNetwork)
class SalesNetworkAdmin(admin.ModelAdmin):

    list_display = ('level', 'name', 'email', 'city', 'supplier', 'debt')
    list_filter = ('city',)
    actions = ('clear_debt',)

    def clear_debt(self, queryset):
        queryset.update(debt=0)
