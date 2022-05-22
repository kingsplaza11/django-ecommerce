from django.urls import path
from .views import *
from . import views


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('product/<slug>/', ProductDetailView.as_view(), name='product'),
    path('add-to-cart/<slug>/', add_to_cart, name='add-to-cart'),
    path('remove-from-cart/<slug>/', remove_from_cart, name='remove-from-cart'),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path('checkout/', CheckoutView.as_view(), name='checkout'),
    path('order-summary/', OrderSummaryView.as_view(), name='cart'),
    path('request-refund/', RequestRefundView.as_view(), name='request-refund'),
    path('remove-item-from-cart/<slug>/', remove_single_item_from_cart
         , name='remove-single-item-from-cart'),

]
