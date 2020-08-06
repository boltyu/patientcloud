from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index),
    path('<str:idnum>/epos/',views.Epos),
    path('<str:idnum>/pic/',views.Pic),
    path('<str:idnum>/',views.Info)
]