from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
   path('',views.home,name='home'),
   path('login/',views.login_user,name='login'),
   path('logout',views.logout_user,name='logout'),
   path('quote_v1/',views.quote_form_v1,name='q1'),
   path('quote_v2/',views.quote_form_v2,name='q2'),
   path('bill_form/',views.bill_form,name='bform'),
   path('bill_form2/',views.bill_form2,name='bform2'),
   path('los/',views.los,name='los'),
   path('los2',views.los2,name='los2'),
   path('los3',views.los3,name='los3'),
   path('los4',views.los4,name='los4'),
   path('vi/',views.quote,name='q'),
   path('vi2/',views.quote2,name='qv2'),
   path('vi3/',views.b,name='b1'),
   path('vi4/',views.b2,name='b2'),
]