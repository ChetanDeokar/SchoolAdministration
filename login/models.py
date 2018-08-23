# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
# Create your models here.


class UserManager(BaseUserManager):

    def create_student(self, email, password, firstname, lastname, status):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.usertype = 'ST'
        user.firstname = firstname
        user.lastname = lastname
        user.status = status
        user.admin = False
        user.active = True
        user.staff = False
        user.save(using=self._db)
        return user

    def create_teacher(self, email, password, firstname, lastname, status):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.usertype = 'TE'
        user.firstname = firstname
        user.lastname = lastname
        user.status = status
        user.admin = False
        user.active = True
        user.staff = True
        user.save(using=self._db)
        return user

    def create_head_master(self, email, password, firstname, lastname, status):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.usertype = 'HM'
        user.admin = True
        user.active = True
        user.staff = True
        user.firstname = firstname
        user.lastname = lastname
        user.status = status
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(email=self.normalize_email(email))
        user.set_password(password)
        user.usertype = 'HM'
        user.admin = True
        user.staff = True
        user.save(using=self._db)
        return user

    def create_user(self, email, password, usertype, status, firstname, lastname):
        if usertype == 'HM':
            self.create_head_master(email, password, firstname, lastname, status)
        if usertype == 'ST':
            self.create_student(email, password, firstname, lastname, status)
        if usertype == 'TE':
            self.create_teacher(email, password, firstname, lastname, status)


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(verbose_name='email address', max_length=255, unique=True, blank=False)
    usertype = models.CharField(verbose_name="User Type",blank=False,max_length=255, choices=[("HM", "HeadMaster"), ("ST", "Student"), ("TE", "Teacher")])
    status = models.IntegerField(verbose_name="User Status", blank=False, default=1)
    admin = models.BooleanField(blank=False, default=False)
    firstname = models.CharField(blank=False, max_length=255)
    lastname = models.CharField(blank=False,max_length=255)
    staff = models.BooleanField(default=False)
    active = models.BooleanField(default=True)

    objects = UserManager()
    USERNAME_FIELD = 'email'

    @property
    def get_usertype(self):
        choices = dict([("HM", "HeadMaster"), ("ST", "Student"), ("TE", "Teacher")])
        return choices[self.usertype]

    @property
    def get_status(self):
        return self.status

    @property
    def get_name(self):
        return "%s %s" % (self.firstname, self.lastname)

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        return self.staff

    @property
    def is_admin(self):
        "Is the user a admin member?"
        return self.admin

    @property
    def is_active(self):
        "Is the user active?"
        return self.active

    def get_full_name(self):
        # The user is identified by their email address
        return self.email

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def __str__(self):  # __unicode__ on Python 2
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True
