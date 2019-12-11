from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator
from orders.models import Course, History, Tray
from django.utils import timezone

import re
# Create your models here.


class CatrUser(models.Model):
    # this caterer class allows me to extend the existing User model
    # as seen in the line below
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # 0 if caterer, 1 if consumer
    user_type = models.PositiveIntegerField(
        validators=[MinValueValidator(0), MaxValueValidator(1)])

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    created_date = models.DateTimeField('date created')
    email = models.EmailField()
    profile_image = models.ImageField(upload_to='media/',
                                      null=True,
                                      blank=True)


class Caterer(CatrUser):
    business_name = models.CharField(max_length=100)
    business_description = models.CharField(max_length=1000)

    # breaking down address into different parts
    province_address = models.CharField(max_length=100)
    municipality_address = models.CharField(max_length=100)
    street_address = models.CharField(max_length=100)
    zip_code = models.CharField(max_length=10)

    courses = models.ManyToManyField(Course, through='Menu')

    def __str__(self):
        return "Business name: {}".format(self.business_name)

    def has_valid_zip_code(self):
        pattern = re.compile("^\d{4}$")
        if pattern.match(self.zip_code) is not None:
            return True
        return False

    def has_valid_province_address(self):
        pass

    def save(self, *args, **kwargs):
        if self.created_date is None:
            self.created_date = timezone.now()
        return super(Caterer, self).save(*args, **kwargs)

    def asdict(self):
        return {
            'id': self.id,
            'business_name': self.business_name,
            'business_description': self.business_description,
            'province_address': self.province_address,
            'municipality_address': self.municipality_address,
            'street_address': self.street_address,
            'zip_code': self.zip_code,
            'user_type': self.user_type,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_date': self.created_date,
            'email': self.email,
            'profile_image': self.profile_image.url
        }


class Consumer(CatrUser):
    consumer_badge = models.IntegerField(blank=True, null=True)
    history = models.ForeignKey(History, on_delete=models.CASCADE)

    def __str__(self):
        return "Regular user: {} {}".format(self.first_name, self.last_name)

    def is_valid_badge_value(self):
        if self.badge < 0 or self.badge > 1:
            return False
        return True

    def get_present_transaction(self):
        return None

    def save(self, *args, **kwargs):
        if self.created_date is None:
            self.created_date = timezone.now()
        return super(Consumer, self).save(*args, **kwargs)


class Package(models.Model):
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    package_name = models.CharField(max_length=50)
    package_date_created = models.DateTimeField()

    def __str__(self):
        return "{}".format(self.package_name)


class Menu(models.Model):
    # caterer and course keys are for the many-to-many relationship
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    menu_date_added = models.DateField()

    # package key is for the one to many relationship from package
    # # to menu (menu_item)
    package = models.ForeignKey(
        Package,
        on_delete=models.CASCADE,
        null=True,
        blank=True
    )

    def __str__(self):
        # return "{} ::: {} ({}) in package <{}>"\
        return "{} ::: {} ({})"\
            .format(
                self.caterer.business_name,
                self.course.course_name,
                self.course.course_category,
            )

    def save(self, *args, **kwargs):
        if self.menu_date_added is None:
            self.menu_date_added = timezone.now()
        return super(Menu, self).save(*args, **kwargs)


class Transaction(models.Model):
    history = models.ForeignKey(History, on_delete=models.CASCADE)
    tray = models.ForeignKey(Tray, on_delete=models.CASCADE)
    caterer = models.ForeignKey(Caterer, on_delete=models.CASCADE,
                                null=True, blank=True)

    transaction_date = models.DateTimeField()
    transaction_event_date = models.DateTimeField(blank=True, null=True)
    transaction_is_completed = models.BooleanField(blank=True)

    transaction_event_street_location = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )

    transaction_event_building_location = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )

    transaction_event_unit_number = models.CharField(
        blank=True,
        null=True,
        max_length=100
    )

    transaction_other_instructions = models.CharField(
        blank=True,
        null=True,
        max_length=1000
    )

    def __str__(self):
        return "{} --- {}".format(self.history, self.tray)


class Item(models.Model):
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE)
    tray = models.ForeignKey(Tray, on_delete=models.CASCADE)
    item_quantity = models.IntegerField()

    def __str__(self):
        return "{} -- {} :: {}".format(
            self.menu, self.tray, self.item_quantity)


class Image(models.Model):
    image_uploaded_date = models.DateTimeField()
    image_binary = models.ImageField(upload_to="media/")
    image_name = models.CharField(max_length=100)

    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return "{}, owned by: {}"\
            .format(self.image_name,
                    self.menu.caterer.business_name)

    def save(self, *args, **kwargs):
        if self.image_uploaded_date is None:
            self.image_uploaded_date = timezone.now()
        return super(Image, self).save(*args, **kwargs)
