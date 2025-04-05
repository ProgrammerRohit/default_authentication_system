# myapp urls.py

from django.urls import path
from .views import signupView, loginView, profile, logoutView, changepass1, changepass2, updateprofile

urlpatterns = [
    path('signup/',signupView, name='signup'),
    path('login/',loginView, name='login'),
    path('profile/',profile, name='profile'),
    path('logout/',logoutView, name='logout'),
    path('changepass1/',changepass1, name='changepass1'),
    path('changepass2/',changepass2, name='changepass2'),
    path('updateprofile/',updateprofile, name='updateprofile')
]
