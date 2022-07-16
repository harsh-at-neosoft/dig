from rest_framework.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import SignInView,SignUpView,LogoutView

urlpatterns=[
    
    # Get Authentication Token
    path('get-token/',obtain_auth_token,name="get-auth-token"),

    # Sign Up
    path('sign-up/',SignUpView.as_view(),name="user-sign-up"),

    # Sign In
    path('sign-in/',SignInView.as_view(),name="user-sign-in"),

    # Log Out
    path('log-out/',LogoutView.as_view(),name="user-log-out")
]