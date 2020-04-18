from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Message(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)
    phone = models.CharField(max_length=50, null=True, blank=True)
    email = models.EmailField(max_length=50, null=True, blank=True)
    msg = models.TextField(max_length=1000, null=True, blank=True)
    date_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)
    

class ProductCategory(models.Model):
    name = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return str(self.name)


class Product(models.Model):
    sku = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=30)
    sale_price = models.IntegerField()
    original_price = models.IntegerField()
    description = models.TextField(max_length=1000)
    category = models.ForeignKey(ProductCategory, on_delete=models.CASCADE)  # One to Many Relation with ProductCategory
    update_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name) + ' | Price: ' + str(self.sale_price)


class ProductImage(models.Model):
    Product = models.ForeignKey(Product, on_delete=models.CASCADE)  # One to Many Relation with Product
    image = models.ImageField(blank=True, null=True)

    def __str__(self):
        return str(self.image)


class Device(models.Model):
    name = models.CharField(max_length=100)
    owned_by = models.CharField(max_length=100)
    Engine_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    Engine_Brand = models.CharField(max_length=100)
    Engine_Displacement = models.CharField(max_length=100)
    Engine_Maximum_Output = models.CharField(max_length=100)
    Engine_Type = models.CharField(max_length=100)
    Engine_Oil_Alert_System = models.CharField(max_length=100)
    Engine_Ignition_System = models.CharField(max_length=100)
    Engine_Start = models.CharField(max_length=100)
    Generator_Alternator = models.CharField(max_length=100)
    Voltage_Regulator = models.CharField(max_length=100)
    Phase = models.CharField(max_length=100)
    ACMax_Output = models.CharField(max_length=100)
    AC_Rated_Output = models.CharField(max_length=100)
    Rated_Voltage = models.CharField(max_length=100)
    DC_Output = models.CharField(max_length=100)
    Rated_Power_Factor = models.CharField(max_length=100)
    Pilot_Lamp = models.CharField(max_length=100)
    Volt_Meter = models.CharField(max_length=100)
    Fuel_Tank_Capacity = models.IntegerField()
    Continuous_Operating_Hours = models.CharField(max_length=100)
    Dimensions_L_W_H = models.CharField(max_length=100)
    Dry_Weight = models.IntegerField()

    def __str__(self):
        return str(self.name)

class Employee(models.Model):
    emp_User = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emp_user")
    emp_supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name="emp_supervisor")
    device_id = models.ForeignKey(Device, on_delete=models.CASCADE)
    dateOfBirth = models.DateField()
    phone = models.CharField(max_length=30, blank=True, help_text='Contact Phone Number')
    address = models.CharField(max_length=50, blank=True, null=True)
    cnic = models.CharField(max_length=20, null=True, blank=True)
    designation = models.CharField(max_length=50)
    emp_delete = models.BooleanField(default=False)
    emp_type = models.CharField(choices=(
        ('Electrician', 'Electrician'),
        ('Mechanic', 'Mechanic')
    ), max_length=20)


class Sensors(models.Model):
    sensor_name = models.CharField(choices=(
        ('Voltage', 'Voltage'),
        ('Oil level', 'Oil level'),
        ('Temperature', 'Temperature')
    ), max_length=20)
    device = models.ForeignKey(Device, on_delete=models.CASCADE)


class sensor_reading_details(models.Model):
    sensor = models.ForeignKey(Sensors, on_delete=models.CASCADE)
    reading = models.IntegerField()
    created_time = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField(default=False)