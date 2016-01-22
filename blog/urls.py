from django.conf.urls import url, include
import views
from premium_ac.views import paypal_return, paypal_cancel, products
from paypal.standard.ipn import urls as paypal_urls

urlpatterns = [
    url(r'^$', views.get_home),
    url(r'^blog/$', views.post_list, name="post_list"),
    url(r'^blog/(?P<id>\d+)/$', views.post_detail),
    url(r'^post/new/$', views.new_post, name="new_post"),
    url(r'^a-fictional-url/', include(paypal_urls)),
    url(r'^paypal-return/$', paypal_return),
    url(r'^paypal-cancel/$', paypal_cancel),
    url(r'^products/$', products, name='products')
]
