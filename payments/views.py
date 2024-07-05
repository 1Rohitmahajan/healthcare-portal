from django.shortcuts import render
from django.conf import settings
from django.views.generic.base import TemplateView
import stripe

stripe.api_key = settings.STRIPE_SECRET_KEY

class checkout(TemplateView):
    template_name = 'checkout.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["key"] = settings.STRIPE_PUBLISHABLE_KEY
        return context


def charge(request):
    if request.method == "POST":
        try:
            token = request.POST['stripeToken']
            charge = stripe.Charge.create(
                amount=6000,
                currency='inr',
                description='Payment Gateway',
                source=token
            )
        except stripe.error.StripeError as e:
    # Handle other Stripe errors
            return render(request, 'charge.html', {'error': str(e)})
        except Exception as e:
    # Handle other exceptions
            return render(request, 'charge.html', {'error': str(e)})


    return render(request, 'charge.html')


