from django.urls import path
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('colheitas/',views.colheitas, name='listagem_colheitas')
]