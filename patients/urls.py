from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index),
    path('<str:idnum>/<str:category>/',views.Pic),
    path('<str:idnum>/<str:category>/<str:filename>',views.Picfile),
    path('<str:idnum>/',views.Info)
]