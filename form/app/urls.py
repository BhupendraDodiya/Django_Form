from django.urls import path
from app import views

urlpatterns = [
    path('',views.index),
    path('reg/',views.reg,name='registration'),
    path('table/',views.table,name='detail'),
    path('delete/<int:uid>/',views.delete,name='delete'),
    path('edit/<int:uid>/',views.edit,name='update'),
    path('upd/',views.update,name='update'),
]