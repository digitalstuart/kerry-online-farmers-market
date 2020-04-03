from django.conf.urls import url, include
from accounts.views import logout, login_seller, login_buyer, registration, user_profile
from accounts import url_reset

urlpatterns = [
    url(r'^logout/', logout, name="logout"),
    url(r'^seller-login/', login_seller, name="login_seller"),
    url(r'^buyer-login/', login_buyer, name="login_buyer"),
    url(r'^register/', registration, name="registration"),
    url(r'^profile/', user_profile, name="profile"),
    url(r'^password-reset/', include(url_reset))
]