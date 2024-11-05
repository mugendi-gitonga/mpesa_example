"""
URL configuration for daraja project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path

from core.views import MpesaConfirmation, MpesaValidation, STKPush

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/v1/', include([
        path('payment/stk-push/', STKPush.as_view(), name='send-stk-push'),
        path('payment/validation/', MpesaValidation.as_view(), name='payment-validation-view'),
        path('payment/confirmation/', MpesaConfirmation.as_view(), name='payment-confirmation-view'),
    ]))
]
