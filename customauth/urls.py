from django.urls import include, path
from customauth import views
from django.contrib.auth import views as auth_views

urlpatterns = [
	path('', views.loginview),
	path('login/', auth_views.LoginView.as_view(template_name='account/login.html'), name='login'),
	path('logout/', auth_views.LogoutView.as_view(), name='logout'),
	path('signup/', views.signup, name='signup'),
	path('profile/', views.profile, name='profile'),
	path('about/', views.about, name='about'),
	path('contact/', views.contact, name='contact'),
    path('subscription/', views.subscription, name='subscription')
]
