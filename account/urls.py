from django.urls import path
from account.views import userRegistrationView, userLoginView, UserProfileView

urlpatterns = [
    path("register/", userRegistrationView.as_view(), name="register"),
    path("login/", userLoginView.as_view(), name="register"),
    path("profile/", UserProfileView.as_view(), name="profile"),
]
