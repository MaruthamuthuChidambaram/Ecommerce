from django.urls import path
from .views import *

urlpatterns = [
    # Homepage API
    path('', HomePageView.as_view(), name='home_page_view'),
    
]
