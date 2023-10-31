from django.urls import path
from . import views


urlpatterns = [
    path('', views.PortalView.as_view(), name='portal_index'),
    path('login/', views.LoginView.as_view(), name='portal_login'),
    path('logout/', views.LogoutView.as_view(), name='portal_logout'),
    path('register/', views.RegisterView.as_view(), name='portal_register'),
]
