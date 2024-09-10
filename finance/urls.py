from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.login_signup_view, name ='login_signup'),
    path("accounts/",include("django.contrib.auth.urls")),
    # path('',views.login, name ='login'),
    path('home/',views.home, name ='home'),
    path('about/', views.about, name ='about'),
    path('contact/',views.contact, name ='contact'),
    path('blog/',views.blog,name ='blog'),
    path('course/',views.course, name ='course')
]


# login-signup/