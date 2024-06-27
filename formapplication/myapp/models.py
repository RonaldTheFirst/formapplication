from django.db import models

class Customer(models.Model):
    customer_no = models.CharField(max_length=20)
    customer_name = models.CharField(max_length=100)
    customer_surname = models.CharField(max_length=100)
    customer_dob = models.CharField(max_length=20)
    customer_occupation = models.CharField(max_length=100)

    def __str__(self):
        return self.customer_name  # Display name in admin panel

class User(models.Model):
    user_no = models.CharField(max_length=20)
    user_name = models.CharField(max_length=100)
    user_surname = models.CharField(max_length=100)
    user_dob = models.CharField(max_length=20)
    user_role = models.CharField(max_length=100)

    def __str__(self):
        return self.user_name  # Display name in admin panel
