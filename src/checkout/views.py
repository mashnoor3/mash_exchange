from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe
from profiles.models import UserStripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request, **kwargs):
	publish_key = settings.STRIPE_PUBLISHABLE_KEY

	qs = UserStripe.objects.filter(user=request.user)
	user_stripe_obj = qs.first()
	customer_id = user_stripe_obj.stripe_id

	if request.method == 'POST':
		token = request.POST['stripeToken']
		print ('token is {}'.format(token))
		try:
			# Creating customer card
			customer = stripe.Customer.retrieve(customer_id)
			customer.sources.create(source=token)
			# Charge the user's card:
			charge = stripe.Charge.create(
			  amount=599, # value in cents
			  currency="cad",
			  description="Example charge",
			  customer=customer,
			)
		except stripe.error.CardError as e:
			# Card declined
			pass


	context = {'publish_key':publish_key}
	template = 'checkout.html'
	return render (request, template, context)
