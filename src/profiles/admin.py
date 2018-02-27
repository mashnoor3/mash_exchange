from django.contrib import admin
from .models import Profile, UserStripe

class ProfileAdmin (admin.ModelAdmin):
	class Meta:
		model = Profile

admin.site.register(Profile, ProfileAdmin)

class UserStripeAdmin (admin.ModelAdmin):
	class Meta:
		model = UserStripe

admin.site.register(UserStripe, UserStripeAdmin)
