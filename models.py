# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


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


class CancelledOrders(models.Model):
    id = models.BigAutoField(primary_key=True)
    reason = models.TextField(blank=True, null=True)
    cancelled_at = models.DateTimeField()
    order = models.OneToOneField('Orders', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'cancelled_orders'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


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
    user = models.ForeignKey('UserProfiles', models.DO_NOTHING)
    duration = models.CharField(max_length=100, blank=True, null=True)
    profession = models.CharField(max_length=255, blank=True, null=True)
    subject = models.CharField(max_length=255, blank=True, null=True)
    time_slot = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'donations'


class OrderItems(models.Model):
    id = models.BigAutoField(primary_key=True)
    product_name = models.CharField(max_length=255)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    price_at_purchase = models.DecimalField(max_digits=10, decimal_places=2)
    order = models.ForeignKey('Orders', models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'order_items'


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
    user = models.ForeignKey('UserProfiles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders'


class OrdersCart(models.Model):
    id = models.BigAutoField(primary_key=True)
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    user = models.OneToOneField('UserProfiles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'orders_cart'


class OrdersCartitem(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    added_at = models.DateTimeField()
    cart = models.ForeignKey(OrdersCart, models.DO_NOTHING)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    unit_value = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'orders_cartitem'
        unique_together = (('cart', 'product', 'unit_value'),)


class ProductImages(models.Model):
    id = models.BigAutoField(primary_key=True)
    image_url = models.TextField()
    created_at = models.DateTimeField()
    product = models.ForeignKey('Products', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_images'


class ProductReviews(models.Model):
    id = models.BigAutoField(primary_key=True)
    rating = models.IntegerField()
    comment = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField()
    product = models.ForeignKey('Products', models.DO_NOTHING)
    user = models.ForeignKey('UserProfiles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'product_reviews'
        unique_together = (('product', 'user'),)


class ProductVariants(models.Model):
    id = models.BigAutoField(primary_key=True)
    quantity = models.DecimalField(max_digits=10, decimal_places=3)
    unit = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    product = models.ForeignKey('Products', models.DO_NOTHING)
    stock_quantity = models.DecimalField(max_digits=10, decimal_places=3)

    class Meta:
        managed = False
        db_table = 'product_variants'


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
    vendor = models.ForeignKey('UserProfiles', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'products'


class UserAddresses(models.Model):
    id = models.BigAutoField(primary_key=True)
    town_city = models.CharField(max_length=120)
    state = models.CharField(max_length=120)
    country = models.CharField(max_length=120)
    pincode = models.CharField(max_length=10)
    is_default = models.BooleanField()
    created_at = models.DateTimeField()
    user = models.ForeignKey('UserProfiles', models.DO_NOTHING)
    area_street_sector = models.CharField(max_length=255)
    delivery_instructions = models.TextField(blank=True, null=True)
    flat_house_building = models.CharField(max_length=255)
    full_name = models.CharField(max_length=255)
    landmark = models.CharField(max_length=255, blank=True, null=True)
    mobile_number = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'user_addresses'


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
