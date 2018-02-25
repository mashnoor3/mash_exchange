from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

@login_required
def checkout(request):
	publish_key = settings.STRIPE_PUBLISHABLE_KEY
	if request.method == 'POST': 
		token = request.POST['stripeToken']
		print ('token is {}'.format(token))
		try:
			# Charge the user's card:
			charge = stripe.Charge.create(
			  amount=999,
			  currency="cad",
			  description="Example charge",
			  source=token,
			)
		except stripe.error.CardError as e: 
			# Card declined
			pass


	context = {'publish_key':publish_key}
	template = 'checkout.html'
	return render (request, template, context)