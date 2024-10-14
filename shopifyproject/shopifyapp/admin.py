from django.contrib import admin
from .models import Category,Product,Shopify,Cart,CartItem

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Category,CategoryAdmin)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','stock','available']
    list_editable = ['price','stock','available']
    prepopulated_fields = {'slug':('name',)}
    list_per_page = 20
admin.site.register(Product,ProductAdmin)

admin.site.register(Shopify)


class CartAdmin(admin.ModelAdmin):
    list_display = ['cart_id', 'date_added']
admin.site.register(Cart, CartAdmin)


class CartItemAdmin(admin.ModelAdmin):
    list_display = ['product', 'quantity', 'sub_total']
    list_filter = ['cart', 'product']
admin.site.register(CartItem, CartItemAdmin)


