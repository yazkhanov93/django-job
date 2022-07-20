import email
from pyexpat import model
from statistics import mode
from turtle import title
from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Region(models.Model):
    title = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class District(models.Model):
    title = models.CharField(max_length=255)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    body = models.TextField()
    image = models.ImageField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title


class Vacancy(models.Model):
    JOB_TYPE = (
        ("Internship", "Internship"),
        ("Part Time", "Part Time"),
        ("Full Time", "Full Time"),
        ("Remote", "Remote")
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    image = models.ImageField()
    body = models.TextField()
    job_type = models.CharField(max_length=20, choices=JOB_TYPE, default="Full Time")
    region = models.ForeignKey(Region, on_delete=models.SET_NULL, null=True)
    district_or_city = models.ForeignKey(District, on_delete=models.SET_NULL, null=True)
    selary = models.DecimalField(decimal_places=2, max_digits=8)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    def __str__(self):
        return self.title


class Experience(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    company_name = models.CharField(max_length=255)
    years = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class Education(models.Model):
    DEGREE = (
        ('secondary', 'secondary'),
        ('bachelor', 'bachelor'),
        ('master', 'master'),
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    department = models.CharField(max_length=255)
    degree = models.CharField(max_length=20, choices=DEGREE, default="bachelor")
    years = models.CharField(max_length=9)

    def __str__(self):
        return self.title


class AboutUs(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField()
    body = models.TextField()

    def __str__(self):
        return self.title


class Contacts(models.Model):
    title = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=13)    