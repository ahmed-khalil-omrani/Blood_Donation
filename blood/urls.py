from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns=[
    path('logout/',LogoutView.as_view(next_page="login_donor"), name='logout'),
    path('profile_donor/<str:username>/',views.donor_profile,name='donor_profile'),
    path("form/donor/",views.donor_create , name='form_needer'),
    path("connection/",views.connection, name="connection"),
    path('profile_needer/<str:username>/', views.needer_profile , name='needer_profile'),
    path("form/needer/",views.needer_create , name='form_needer'),
    path("donor/login/" , views.login_donor , name='login_donor')
]