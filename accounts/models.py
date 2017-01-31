from __future__ import unicode_literals
from django.utils.translation import ugettext_lazy as _
from django.contrib.gis.db import models
from django.contrib.gis.geos import Point
from django.conf import settings
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser, PermissionsMixin
)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    gen_choices = (
                 ('Male', 'm'),
                 ('Female', 'f')
               )

    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
        null=True,
    )
    name = models.CharField(_("Name"),max_length=150,)
    dob = models.DateField(_("Date of Birth"),blank=True,null=True)
    is_active = models.BooleanField(_("Is Active"),default=True)
    is_admin = models.BooleanField(_("Is Admin"),default=False)
    facebook_id = models.CharField(_("Facebook Id"),max_length=100,blank=True,db_index=True)
    date_joined = models.DateTimeField(_("Date Joined"), auto_now_add=True)
    image_url = models.URLField(_("Image Url"),blank=True,null=True)
    gender = models.CharField(_("Gender"),choices=gen_choices,max_length=5,default="")
    language = models.CharField(max_length=10, default='en',choices=settings.LANGUAGES)
    objects = UserManager()

    USERNAME_FIELD = 'email'

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')
        ordering = ('email',)

    
    def __unicode__(self):
        return unicode(self.name or self.contact_no,)



    def get_image_url(self):
    	if self.image:
    		return self.image.url
    	return self.image_url

    def get_short_name(self):
        # The user is identified by their email address
        return self.email

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin


