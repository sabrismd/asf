from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_user,name='login'),
   path('logout',views.logout_user,name='logout'),
   path('quote_v1/',views.quote_form_v1,name='q1'),
   path('los/',views.los,name='los'),
   path('vi/',views.quote,name='q')
]