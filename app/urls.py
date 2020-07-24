from django.urls import path
from .views import index, HomeView

app_name = 'app'

urlpatterns = [
    path('', index, name='index'),
    path('home/', HomeView.as_view(), name='home')
]
