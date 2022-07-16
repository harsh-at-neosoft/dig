from django.urls import path,include
from .views import secretJoke1,secretJoke2,secretJoke3

urlpatterns=[

    # Users
    path('user/',include('users.urls')),
    
    # Protected Routes with // Session Authentication //
    path('secret-session-joke-1/',secretJoke1,name="secret-joke-1"),
    path('secret-session-joke-2/',secretJoke2,name="secret-joke-2"),
    path('secret-session-joke-3/',secretJoke3,name="secret-joke-3")

]