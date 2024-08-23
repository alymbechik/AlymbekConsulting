from django.urls import path
from . import views


urlpatterns = [
    path('', views.index_view, name='index'),
    path('villa_create/', views.villa_create),
    path('villa_create2/', views.villa_create2),
    path('villa_detail/<int:pk>/', views.villa_detail, name='detail'),
    path('villa_delete/<int:pk>/', views.villa_delete, name='delete')
]
