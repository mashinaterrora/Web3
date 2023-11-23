from django.urls import path
from . import views


urlpatterns = [
    path('', views.index),
    path('login', views.qrpage, name = "Code"),
    path('reg', views.regpage, name = "Reg"),
    path('cabinet', views.regcon, name = "Regconfirm")
]