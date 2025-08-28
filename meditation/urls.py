from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('meditation/', views.meditation, name='meditation'),
    path("contact/", views.contact_view, name="contact"),
    path('therapy/', views.therapy, name='therapy'),
    path("therapy_detail/<str:therapy_type>/", views.therapy_detail, name="therapy_detail"),
    path('approach_form/', views.approach_form, name='approach_form'),
   path('pay/', views.pay, name='pay'),
   path('trial/', views.trial, name='trial'),
   path('login/', views.login_view, name='login'),
   path('logout/', views.logout_view, name='logout'),
   path('signup/', views.signup_view, name='signup'),
]

