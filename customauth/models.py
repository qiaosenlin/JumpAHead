from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin




class UserManager(BaseUserManager):
    def create_user(self, username, email, password=None, **kwargs):
        """
        Creates and saves a User with the given email, date of
        birth and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            username=username,
            email=self.normalize_email(email),
            **kwargs,
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, *args, **kwargs):
        """
        Creates and saves a superuser with the given email, date of
        birth and password.
        """
        return self.create_user(
            *args,
            is_staff=True,
            is_superuser=True,
            **kwargs,
        )


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(
        help_text=_('The name the user logs in as.'),
        max_length=100,
        unique=True,
        verbose_name=_('username'),
    )
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    first_name = models.CharField(
        help_text=_("The user's first name."),
        max_length=100,
        verbose_name=_('first name'),
        blank=True,
    )
    last_name = models.CharField(
        help_text=_("The user's last name."),
        max_length=100,
        blank=True,
        verbose_name=_('last name'),
    )
    is_active = models.BooleanField(
        default=True,
        help_text=_('A boolean indicating if the user account is active. '
                    'Inactive accounts cannot perform actions on the site.'),
        verbose_name=_('is active'),
    )
    is_staff = models.BooleanField(
        default=False,
        help_text=_('A boolean indicating if the user is allowed to access '
                    'the admin site.'),
        verbose_name=_('is staff'),
    )
    is_superuser = models.BooleanField(
        default=False,
        help_text=_('A boolean indicating if the user has all permissions '
                    'without them being explicitly granted.'),
        verbose_name=_('is superuser'),
    )
    time_created = models.DateTimeField(
        auto_now_add=True,
        help_text=_('The time the user was created.'),
        verbose_name=_('time created'),
    )
    time_updated = models.DateTimeField(
        auto_now=True,
        help_text=_('The time the user was last updated.'),
        verbose_name=_('time updated'),
    )
    date_of_birth = models.DateField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    active_subscription = models.BooleanField(default=False)
    subscription_start_date = models.DateField(blank=True, null=True)
    subscription_end_date = models.DateField(blank=True, null=True)


    objects = UserManager()

    REQUIRED_FIELDS = ['email']
    USERNAME_FIELD = 'username'

    def __repr__(self):
        """
        Get a string representation of the user.
        Returns:
            A string containing the information required to reconstruct
            the user.
        """
        return f'User(id={self.id:r}, username={self.username:r})'

    def __str__(self):
        """
        Get a string identifying the user.
        Returns:
            The user's name.
        """
        return f'{self.first_name} {self.last_name}'
