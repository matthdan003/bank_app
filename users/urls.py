from django.urls import path
from .views import index, LoginView, RegisterView, logout

app_name = 'users'

urlpatterns = [
    path('', index, name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout, name='logout')
]
