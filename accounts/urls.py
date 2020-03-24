from django.conf.urls import url, include
from accounts.views import logout, login_seller, login_buyer, registration_buyer, registration_seller, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^seller-login/', login_seller, name="login_seller"),
    url(r'^buyer-login/', login_buyer, name="login_buyer"),
    url(r'^seller-register/', registration_seller, name="registration_seller"),
    url(r'^buyer-register/', registration_buyer, name="registration_buyer"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]