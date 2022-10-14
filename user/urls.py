from django.urls import path
from user import views

urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_in,name='login'),
    path('home/',views.home,name='home'),
]