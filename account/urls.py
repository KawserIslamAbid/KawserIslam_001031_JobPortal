from django.urls import path
from .views import *


urlpatterns = [
    path('login/', login, name='login'),
    path('logout/', signout, name='logout'),
    path('registration/', signup, name='registration'),
    
]