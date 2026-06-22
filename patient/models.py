from django.db import models
from django.contrib.auth.models import User


class Patient(models.Model):

    STATUS_CHOICES = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
        ('Discharged', 'Discharged'),
    )

    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female'),
        ('Other', 'Other'),
    )

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='patients'
    )

    patient_id = models.CharField(max_length=50, unique=True, blank=True)
    patient_name = models.CharField(max_length=255)
    cnic = models.CharField(max_length=15)
    phone = models.CharField(max_length=20)
    email = models.EmailField(blank=True, null=True)

    prescription = models.TextField(blank=True, default="")

    gender = models.CharField(
        max_length=10,
        choices=GENDER_CHOICES
    )

    date_of_birth = models.DateField()

    blood_group = models.CharField(
        max_length=10,
        blank=True,
        null=True
    )

    address = models.TextField()

    assigned_doctor = models.CharField(
        max_length=255,
        blank=True,
        null=True
    )

    fee = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0.00
    )

    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='Active'
    )

    date = models.DateField(auto_now_add=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.patient_name