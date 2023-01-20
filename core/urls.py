from .views import IndexView, TesteView, Erro500
from django.urls import path


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('teste/', TesteView.as_view(), name='404'),
    path('error-serve/', Erro500.as_view(), name='500')
]
