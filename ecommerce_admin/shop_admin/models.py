from django.db import models
from django.core.files.storage import default_storage
from django.conf import settings
class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'

class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)

class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)

class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'

class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)

class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)

class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)

class UserProfiles(models.Model):
    id = models.BigAutoField(primary_key=True)
    full_name = models.CharField(max_length=255)
    mobile_number = models.CharField(unique=True, max_length=20)
    password_hash = models.TextField()
    gender = models.CharField(max_length=20, blank=True, null=True)
    category = models.CharField(max_length=30)
    address_line = models.TextField(blank=True, null=True)
    city = models.CharField(max_length=120, blank=True, null=True)
    state = models.CharField(max_length=120, blank=True, null=True)
    country = models.CharField(max_length=120, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    location_url = models.TextField(blank=True, null=True)
    profile_pic_url = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user_profiles'
        verbose_name_plural = 'User Profiles'
        
    def __str__(self):
        return f"{self.full_name} ({self.mobile_number})"

class Products(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    unit = models.CharField(max_length=50)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=3)
    average_rating = models.DecimalField(max_digits=3, decimal_places=2)
    rating_count = models.IntegerField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    vendor = models.ForeignKey(UserProfiles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products'
        verbose_name_plural = 'Products'
        
    def __str__(self):
        return self.name

class Orders(models.Model):
    id = models.BigAutoField(primary_key=True)
    shipping_address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=20)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20)
    payment_method = models.CharField(max_length=20)
    is_paid = models.BooleanField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.ForeignKey(UserProfiles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'
        verbose_name_plural = 'Orders'
        
    def __str__(self):
        return f"Order #{self.id} by {self.user.full_name}"

class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey(Orders, models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'
        verbose_name_plural = 'Order Items'
        
    def __str__(self):
        return f"{self.quantity}x {self.product_name}"

class ProductImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_url = models.TextField()
    created_at = models.DateTimeField()
    product = models.ForeignKey(Products, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_images'
        verbose_name_plural = 'Product Images'
        
    def __str__(self):
        return f"Image for {self.product.name}"

class ProductReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    product = models.ForeignKey(Products, models.DO_NOTHING)
    user = models.ForeignKey(UserProfiles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_reviews'
        verbose_name_plural = 'Product Reviews'
        unique_together = (('product', 'user'),)
        
    def __str__(self):
        return f"{self.rating} star review for {self.product.name} by {self.user.full_name}"

class ProductVariants(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'product_variants'
        verbose_name_plural = 'Product Variants'

class UserAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    town_city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    pincode = models.CharField(max_length=10)
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    user = models.ForeignKey(UserProfiles, models.DO_NOTHING)
    area_street_sector = models.CharField(max_length=255)
    delivery_instructions = models.TextField(blank=True, null=True)
    flat_house_building = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_addresses'
        verbose_name_plural = 'User Addresses'
        
    def __str__(self):
        return f"Address for {self.user.full_name}"

class Donations(models.Model):
    id = models.BigAutoField(primary_key=True)
    donation_type = models.CharField(max_length=20)
    status = models.CharField(max_length=20)
    created_at = models.DateTimeField()
    item_name = models.CharField(max_length=255, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    quantity = models.CharField(max_length=100, blank=True, null=True)
    item_image = models.CharField(max_length=100, blank=True, null=True)
    pickup_address = models.TextField(blank=True, null=True)
    contact_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.CharField(max_length=255, blank=True, null=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    payment_screenshot = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField(blank=True, null=True)
    user = models.ForeignKey(UserProfiles, models.DO_NOTHING)
    duration = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    time_slot = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donations'
        verbose_name_plural = 'Donations'
        
    def __str__(self):
        return f"{self.donation_type} donation by {self.user.full_name}"

class CancelledOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.TextField(blank=True, null=True)
    cancelled_at = models.DateTimeField()
    order = models.OneToOneField(Orders, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cancelled_orders'
        verbose_name_plural = 'Cancelled Orders'

class OrdersCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField(UserProfiles, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_cart'
        verbose_name_plural = 'Order Carts'

class OrdersCartitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    added_at = models.DateTimeField()
    cart = models.ForeignKey(OrdersCart, models.DO_NOTHING)
    product = models.ForeignKey(Products, models.DO_NOTHING)
    unit_value = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'orders_cartitem'
        unique_together = (('cart', 'product', 'unit_value'),)
        verbose_name_plural = 'Order Cart Items'

class AutoScrollImage(models.Model):
    PLACEMENT_CHOICES = [
        ('top', 'Top/Upper Scrollbar'),
        ('bottom', 'Bottom/Lower Scrollbar'),
        ('other', 'Other/General')
    ]

    image = models.ImageField(upload_to='auto_scroll_images/', blank=True, null=True, help_text="Upload image here; it will be stored in Cloudinary")
    image_url = models.URLField(max_length=500, blank=True, null=True, help_text="Cloudinary URL link (auto-generated upon save)")
    title = models.CharField(max_length=255, blank=True, null=True, help_text="Optional title for the image")
    placement = models.CharField(max_length=20, choices=PLACEMENT_CHOICES, default='top', help_text="Which slider this image belongs to")
    is_active = models.BooleanField(default=True, help_text="Set to False to hide this image from the scroll")
    order = models.IntegerField(default=0, help_text="Lower numbers appear first")
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        managed = True
        db_table = 'auto_scroll_images'
        verbose_name = 'Auto Scroll Image'
        verbose_name_plural = 'Auto Scroll Images'
        ordering = ['order', '-created_at']

    def save(self, *args, **kwargs):
        # Allow the image to be saved to Cloudinary first
        super().save(*args, **kwargs)
        
        if self.image:
            try:
                # After saving, django-cloudinary-storage generates the complete URL natively
                # self.image.url is available and correctly points to the https:// string
                exact_url = getattr(self.image, 'url', None)
                
                if not exact_url and self.image.name:
                    cloud_name = settings.CLOUDINARY_STORAGE.get('CLOUD_NAME')
                    if cloud_name:
                        exact_url = f"https://res.cloudinary.com/{cloud_name}/image/upload/{self.image.name}"
                
                if exact_url and self.image_url != exact_url:
                    self.image_url = exact_url
                    super().save(update_fields=['image_url'])
            except Exception as e:
                print(f"Cloudinary Save Error: {e}")

    def __str__(self):
        return self.title if self.title else f"Scroll Image #{self.id}"
