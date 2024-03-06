from django.urls import path
from .views import *


urlpatterns = [
    path('', home, name='home'),
    path('add-job/', add_job, name='add_job'),
    path('aprofile/', profile, name='profile'),
    path('list-job/', job_list, name='job_list'),
    path('apply-job/', apply_job_list, name='apply_job_list'),
    path('apply/<int:pk>/', apply_job, name='apply_job'),
]