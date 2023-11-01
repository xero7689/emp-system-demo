from django.db import models
from django.conf import settings
from django.contrib.auth.models import AbstractUser


class Department(models.Model):
    title = models.CharField(unique=True, max_length=128)
    slug = models.SlugField(unique=True, max_length=128)
    description = models.TextField(
        verbose_name="Department Description"
    )
    active = models.BooleanField(
        default=True,
        verbose_name="Department Active Status"
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Employee Data Created DateTime'
    )

    last_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Employee Data Modified DateTime'
    )

    def __str__(self):
        return self.title


class Role(models.Model):
    title = models.CharField(unique=True, max_length=64)
    slug = models.SlugField(unique=True, max_length=128)
    description = models.TextField(verbose_name="Role Description")
    active = models.BooleanField(
        default=True, verbose_name="Role Active Status")

    created_at = models.DateTimeField(
        auto_now_add=True,
        editable=False,
        verbose_name='Employee Data Created DateTime'
    )

    last_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Employee Data Modified DateTime'
    )

    def __str__(self):
        return self.title


class User(AbstractUser):
    phone_number = models.CharField(max_length=24)
    address = models.TextField()

    last_modified = models.DateTimeField(
        auto_now=True,
        editable=False,
        verbose_name='Employee Data Modified DateTime'
    )


class Employee(models.Model):
    class ServiceStatus(models.IntegerChoices):
        RESIGNED = 0
        AT_WORK = 1
        UNPAID_LEAVE = 2

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE
    )
    role = models.ForeignKey(Role, related_name='employees', on_delete=models.PROTECT)
    date_of_hire = models.DateField(verbose_name="Hiring Date")
    service_status = models.IntegerField(
        choices=ServiceStatus.choices, verbose_name="Service Status")
    department = models.ForeignKey(
        Department, related_name='employees', on_delete=models.PROTECT)

    def __str__(self):
        return f'[{self.department.title}] {self.user.username}'

    class Meta:
        indexes = [
            models.Index(fields=['service_status', 'department'])
        ]
