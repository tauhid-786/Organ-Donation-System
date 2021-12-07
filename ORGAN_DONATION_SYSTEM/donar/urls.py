from .views import *
from django.conf.urls import url
from django.urls import path,include
from .models import Donar
app_name='donar'

urlpatterns=[
    path('',Home,name='home'),
    path('cornea/',Cornea,name='cornea'),
    path('heart/',Heart,name='heart'),
    path('intestine/',Intestine,name='intestine'),
    path('kidney/',Kidney,name='kidney'),
    path('liver/',Liver,name='liver'),
    path('lungs/',Lungs,name='lungs'),
    path('pancrease/',Pancrease,name='pancrease'),
    path('tissue/',Tissue,name='tissue'),
    path('login/',Login.as_view(),name='login'),
    path('signup/', Signup.as_view(), name='signup'),
    path('logout/',Logout,name='logout'),
    path('donate/', Donate.as_view(), name='donate'),
    path('available/', Available.as_view(), name='availble'),

]