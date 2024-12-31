from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models import F
from django_otp.plugins.otp_totp.models import TOTPDevice


class CustomUser(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('farmer', 'Farmer'),
        ('outlet', 'outlet'),
        ('franchisee', 'Franchisee'),
    )

    phone = models.CharField(max_length=15, blank=True, null=True)
    aadhaar = models.CharField(max_length=20, blank=True, null=True)
    farmer_card = models.CharField(max_length=20, blank=True, null=True)
    district = models.CharField(max_length=20, blank=True, null=True)
    credit = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    role = models.CharField(max_length=10, choices=ROLE_CHOICES)
    two_factor_enabled = models.BooleanField(default=False)

# class UserTOTPDevice(TOTPDevice):
#     user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)    

class FarmerDetail(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE, primary_key=True)
    phone = models.CharField(max_length=15, blank=True, null=True)
    pincode = models.CharField(max_length=10, blank=True, null=True)
    village = models.CharField(max_length=100, blank=True, null=True)
    taluk = models.CharField(max_length=100, blank=True, null=True)
    district = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=100, blank=True, null=True)
    country = models.CharField(max_length=100, blank=True, null=True)
    # Add other relevant fields


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='category_images/', null=True, blank=True)
    description = models.TextField(blank=True)
    def __str__(self):
        return self.name



class AgriProduct(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    crop_name = models.CharField(max_length=100)
    actual_production = models.DecimalField(max_digits=10, decimal_places=2)
    project_production = models.DecimalField(max_digits=10, decimal_places=2)
    projection_timeline = models.DecimalField(max_digits=10, decimal_places=2)
    cultivation_land_value = models.DecimalField(max_digits=10, decimal_places=2)
    cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    project_cost_per_unit = models.DecimalField(max_digits=10, decimal_places=2)
    image = models.ImageField(upload_to='agri_product_images/', null=True, blank=True)

    def __str__(self):
        return f"{self.crop_name} by {self.user.username}"


class AgriAsset(models.Model):
    # Fields
    land_owner = models.CharField(max_length=255)
    land_location = models.CharField(max_length=255)
    google_map_location = models.URLField(max_length=500, blank=True, null=True)
    width = models.FloatField()
    length = models.FloatField()
    size = models.FloatField()

    # Choices for cultivation_method
    NANCHAI = 'Nanchai'
    PUNCHAI = 'Punchai'
    CULTIVATION_METHOD_CHOICES = [
        (NANCHAI, 'Nanchai'),
        (PUNCHAI, 'Punchai'),
    ]
    cultivation_method = models.CharField(
        max_length=10,
        choices=CULTIVATION_METHOD_CHOICES,
        default=NANCHAI,
    )

    # Choices for owner_type
    OWN = 'own'
    LEASE = 'lease'
    OWNER_TYPE_CHOICES = [
        (OWN, 'Own'),
        (LEASE, 'Lease'),
    ]
    owner_type = models.CharField(
        max_length=5,
        choices=OWNER_TYPE_CHOICES,
        default=OWN,
    )

    def __str__(self):
        return f"{self.land_owner} - {self.land_location}"
    


class Contact(models.Model):
    # Fields
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    referral = models.CharField(max_length=255, blank=True, null=True)
    
    
    
def __str__(self):
        return self.name

