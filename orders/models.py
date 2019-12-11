from django.db import models
# Create your models here.


class Course(models.Model):
    course_name = models.CharField(max_length=50)
    course_description = models.CharField(max_length=200)
    course_category = models.CharField(max_length=200)
    course_unit = models.CharField(max_length=20)
    course_price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return "{} in <{}>".format(self.course_name, self.course_category)


class Tray(models.Model):
    created_date = models.DateTimeField("Date used")
    tray_cumulative_price = models.DecimalField(decimal_places=2, max_digits=7)

    def __str__(self):
        return "Price: PHP {}".format(self.tray_cumulative_price)


class History(models.Model):
    history_points = models.IntegerField()

    def __str__(self):
        return "Points: {}".format(self.history_points)
