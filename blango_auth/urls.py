from django.urls import path, include
from django_registration.backends.activation.views import RegistrationView
from .forms import BlangoRegistrationForm
from . import views

urlpatterns =[
  path("accounts/", include("django.contrib.auth.urls")),
  path("accounts/profile/", views.profile, name="profile"),
  path(
    "accounts/register/",
    RegistrationView.as_view(form_class=BlangoRegistrationForm),
    name="django_registration_register",
),
path("accounts/", include("django_registration.backends.activation.urls")),
]

