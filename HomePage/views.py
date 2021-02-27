from django.shortcuts import render
from django.views.generic import TemplateView
from django.conf import settings
from .models import Product


# Create your views here.
class HomePageView(TemplateView):
    template_name = "homepage.html"

    def get_context_data(self, **kwargs):
        products = Product.objects.filter(price__gte=0).order_by('name')
        context = super(HomePageView, self).get_context_data(**kwargs)
        context.update({
            "products": products,
            "STRIPE_PUBLIC_KEY": settings.STRIPE_PUBLIC_KEY
        })
        return context