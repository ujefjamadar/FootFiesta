from django.contrib import admin
from footapp.models import *
# Register your models here.
class ShoeProductAdmin(admin.ModelAdmin):
    list_display=['shoename','detail','price','cat','is_active']
    list_filter=['cat','is_active']
admin.site.register(ShoesProduct,ShoeProductAdmin)

class PlaceOrderAdmin(admin.ModelAdmin):
    list_display = ['uid', 'fullname', 'status', 'order_date']  
    fields = ('uid', 'fullname', 'mobile', 'email', 'address', 'city', 'state', 'zip', 'order_date', 'total_amount', 'status')

    def get_readonly_fields(self, request, obj=None):
        if obj:  
            return ['uid', 'fullname', 'mobile', 'email', 'address', 'city', 'state', 'zip', 'order_date', 'total_amount']  # Make these fields read-only
        return []  

    def has_add_permission(self, request):
        return False  # Prevent adding new orders

    def has_change_permission(self, request, obj=None):
        if obj:  
            return True  
        return False  

admin.site.register(PlaceOrder, PlaceOrderAdmin)