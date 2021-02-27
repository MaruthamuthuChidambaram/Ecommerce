from django.views.generic import TemplateView
import stripe
from django.conf import settings
from django.http import JsonResponse
from django.views import View
from HomePage.models import Product
from django.views.decorators.csrf import csrf_exempt # new
from django.http.response import JsonResponse # new


stripe.api_key = settings.STRIPE_SECRET_KEY

class CreateCheckoutSessionView(View):
    def get(self, request, *args, **kwargs):
        try:
            product_id = self.kwargs["pk"]
            product = Product.objects.get(id=product_id)
            checkout_session = stripe.checkout.Session.create(
                success_url=settings.DOMAIN + 'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=settings.DOMAIN + 'cancel/',
                payment_method_types=['card'],
                mode='payment',
                line_items=[
                    {
                        'name': product.name,
                        'quantity': 1,
                        'currency': 'usd',
                        'amount': product.price,
                    }
                ]
            )
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            return JsonResponse({'error': str(e)})

class SuccessView(TemplateView):
    template_name = "success.html"

class CancelView(TemplateView):
    template_name = "cancel.html"

