from __future__ import unicode_literals
from django.db import models
from django.conf import settings
from allauth.account.signals import user_logged_in, user_signed_up
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class Profile(models.Model):
	name = models.CharField(max_length=120)
	user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, blank=True)
	location = models.CharField(max_length=120, default='description default text', blank=True, null=True )

	def __unicode__(self):
		return self.name

	# def __str__(self):
	# 	return self.name

class UserStripe(models.Model):
	user = models.OneToOneField(settings.AUTH_USER_MODEL)
	stripe_id = models.CharField(max_length=200, null=True, blank=True)

	def __unicode__(self):
		if self.stripe_id:
			return str(self.stripe_id)
		else:
			return self.user.username

# def my_callback(sender, **kwargs):
# 	user = kwargs["user"]
# 	id_stripe, created = UserStripe.objects.get_or_create(user = user)
# 	if created:
# 		print ("created stripe id for %s"%(user.username))
# 	user_profile, is_created = Profile.objects.get_or_create(user = user)
# 	if is_created:
# 		user_profile.name = user.username
# 		user_profile.save()

def stripe_call_back (sender, **kwargs):
	user = kwargs["user"]
	user_stripe_acc, created = UserStripe.objects.get_or_create(user=user)
	if created:
		print ("created stripe id for %s" %(user.username))
	if user_stripe_acc.stripe_id is None or user_stripe_acc.stripe_id == '':
		new_stripe_id = stripe.Customer.create(email=user.email)
		user_stripe_acc.stripe_id = new_stripe_id['id']
		user_stripe_acc.save()

def profile_call_back (sender, **kwargs):
	user = kwargs["user"]
	user_profile, is_created = Profile.objects.get_or_create(user=user)
	if is_created:
		user_profile.name = user.username
		user_profile.save()

user_logged_in.connect(stripe_call_back)
user_signed_up.connect(profile_call_back)
user_signed_up.connect(stripe_call_back)
# user_logged_in.connect(my_callback)
