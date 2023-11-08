from django.contrib import admin
from django.urls import path,include
from . import views
app_name='bookapp'

urlpatterns = [
    path('',views.index,name='index'),
    path('book/<int:book_no>/',views.detail,name='detail'),
    path('add/',views.add_book,name='add_book'),
    path('update/<int:book_no>/',views.update,name='update'),
    path('delete/<int:book_no>/',views.delete,name='delete'),
    path('button-click/',views.handle_btn_click,name='handle_btn_click'),
]
