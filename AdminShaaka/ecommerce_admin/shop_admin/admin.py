from django.contrib import admin
from .models import (
    Products, Orders, OrderItems, UserProfiles, Donations, ProductImages,
    ProductReviews, ProductVariants, UserAddresses, CancelledOrders, OrdersCart, OrdersCartitem,
    AutoScrollImage
)

# Inlines
class ProductImagesInline(admin.TabularInline):
    model = ProductImages
    extra = 1

class ProductVariantsInline(admin.TabularInline):
    model = ProductVariants
    extra = 1

class OrderItemsInline(admin.TabularInline):
    model = OrderItems
    extra = 0
    readonly_fields = ('product_name', 'quantity', 'price_at_purchase', 'product')
    can_delete = False

# Model Admins
@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'category', 'price', 'stock_quantity', 'average_rating')
    search_fields = ('name', 'description', 'category')
    list_filter = ('category',)
    inlines = [ProductImagesInline, ProductVariantsInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'payment_method', 'is_paid', 'created_at')
    search_fields = ('id', 'user__full_name', 'user__mobile_number', 'status')
    list_filter = ('status', 'is_paid', 'payment_method', 'created_at')
    inlines = [OrderItemsInline]
    readonly_fields = ('created_at', 'updated_at')

@admin.register(UserProfiles)
class UserProfilesAdmin(admin.ModelAdmin):
    list_display = ('id', 'full_name', 'mobile_number', 'category', 'city')
    search_fields = ('full_name', 'mobile_number', 'city', 'state')
    list_filter = ('category',)
    readonly_fields = ('created_at', 'updated_at')

@admin.register(Donations)
class DonationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'donation_type', 'user', 'item_name', 'status', 'amount', 'created_at')
    search_fields = ('item_name', 'user__full_name', 'user__mobile_number', 'donation_type')
    list_filter = ('donation_type', 'status', 'created_at')

@admin.register(ProductReviews)
class ProductReviewsAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'user', 'rating', 'created_at')
    search_fields = ('product__name', 'user__full_name', 'comment')
    list_filter = ('rating', 'created_at')

@admin.register(UserAddresses)
class UserAddressesAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'full_name', 'mobile_number', 'town_city', 'is_default')
    search_fields = ('user__full_name', 'full_name', 'mobile_number', 'town_city', 'pincode')

@admin.register(CancelledOrders)
class CancelledOrdersAdmin(admin.ModelAdmin):
    list_display = ('id', 'order', 'cancelled_at')
    search_fields = ('order__id',)

@admin.register(OrdersCart)
class OrdersCartAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'updated_at')
    search_fields = ('user__full_name',)

@admin.register(OrdersCartitem)
class OrdersCartitemAdmin(admin.ModelAdmin):
    list_display = ('id', 'cart', 'product', 'quantity', 'unit_value')
    search_fields = ('product__name', 'cart__user__full_name')

@admin.register(AutoScrollImage)
class AutoScrollImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image', 'image_url', 'placement', 'is_active', 'order', 'created_at')
    list_editable = ('placement', 'is_active', 'order')
    list_filter = ('placement', 'is_active', 'created_at')
    search_fields = ('title', 'image_url')
