from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# from django.conf import settings
# Create your models here.


class User(AbstractUser):
    groups = models.ManyToManyField(Group, related_name='+')
    user_permissions = models.ManyToManyField(Permission, related_name='+')

    class Meta:
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        pass


class Principle(AbstractUser):
    tsc = models.CharField(max_length=20, blank=True, null=True)
    telNo = models.CharField(max_length=20, blank=True, null=True)
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)
    groups = models.ManyToManyField(Group, related_name='+')
    user_permissions = models.ManyToManyField(Permission, related_name='+')

    class Meta:
        managed = True
        verbose_name = "Principle"
        verbose_name_plural = "Principles"

    def __str__(self):
        return self.username

    def __unicode__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField()
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categorys"

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    description = models.TextField()
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Status"
        verbose_name_plural = "Statuss"

    def __str__(self):
        return self.name


class SubCounty(models.Model):
    name = models.CharField(max_length=20, blank=False, null=False)
    code = models.CharField(max_length=20, blank=True, null=True)
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "SubCounty"
        verbose_name_plural = "SubCountys"

    def __str__(self):
        return self.name


class School(models.Model):
    school_types = (
        ('PR', 'Primary'),
        ('SC', 'Secondary'),
    )
    name = models.CharField(max_length=20, blank=True, null=True)
    knecCode = models.CharField(
        max_length=20, blank=True, null=True)
    principle = models.ForeignKey(Principle, blank=True, null=True, on_delete=models.CASCADE)
    subCounty = models.ForeignKey(SubCounty, blank=True, null=True, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, blank=True, null=True, on_delete=models.CASCADE)
    status = models.ForeignKey(Status, blank=True, null=True, on_delete=models.CASCADE)
    sType = models.CharField(max_length=10, choices=school_types, default="SC")
    streams = models.PositiveIntegerField(default=1)
    enrollment = models.PositiveIntegerField(default=1)
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name


class Capacity(models.Model):
    gender = (
        ('B', 'Boys'),
        ('G', 'Girls'),
    )
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    year = models.CharField(max_length=4, blank=False, null=False)
    gender = models.CharField(
        max_length=5, choices=gender, blank=False, null=False)
    amount = models.PositiveIntegerField(default=0)
    lastEdit = models.DateTimeField(auto_now=True)
    firstInput = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Capacity"
        verbose_name_plural = "Capacitys"

    def __str__(self):
        return "%s school %s year %s gender" % (
            self.school.name, self.year, self.gender)
