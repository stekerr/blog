from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from paypal.standard.forms import PayPalPaymentsForm
from django.conf import settings
import uuid
from blog.models import Product


@csrf_exempt
def paypal_return(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal_return.html', args)


def paypal_cancel(request):
    args = {'post': request.POST, 'get': request.GET}
    return render(request, 'paypal_cancel.html', args)


@property
def paypal_form(self):
    paypal_dict = {
        "business": "steve@business.com",
        "amount": "12.00",
        "item_name": "Premium Account",
        "invoice": "%s-%s" % (self.pk, uuid.uuid4()),
        "notify_url": settings.PAYPAL_NOTIFY_URL,
        "return_url": "%s/paypal-return/" % settings.SITE_URL,
        "cancel_return": "%s/paypal-cancel/" % settings.SITE_URL,
    }

    return PayPalPaymentsForm(initial=paypal_dict)


def products(request):
    var = Product.objects.all()
    return render(request, "products.html", {'products': var})
