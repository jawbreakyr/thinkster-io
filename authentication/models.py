from django.db import models
from django.contrib.auth.models import AbstractBaseUser


"""
	instead of extending the User model, i extended out from AbstractBaseUser
	which is the abstract model used by the User model so the 'tagline' field 
	can be added.
"""
class Account(AbstractBaseUser):
	email = models.EmailField(unique=True)
	username = models.CharField(max_length=40, unique=True)

	first_name = models.CharField(max_length=40, blank=True)
	last_name = models.CharField(max_length=40, blank=True)
	tagline = models.CharField(max_length=140, blank=True)

	is_admin = models.BooleanField(default=False)

	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)

	objects = AccountManager()

	# sets the 'email' field as the username used for logging in
	# requiring the email field to be unique=True
	USERNAME_FIELD = 'email'

	REQUIRED_FIELDS = ['username']

	def __unicode__(self):
		return self.email

	def get_full_name(self):
		return ' '.join([self.first_name, self.last_name])

	def get_short_name(self):
		return self.first_name