from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.index,name='index'),
    path('buy/',views.user,name='buy'),
    path('pdf/<int:pk>',views.pdf,name='pdf'),
]