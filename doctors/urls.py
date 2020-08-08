from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index),
    path('login',views.PageLogin),
    path('login/',views.Login),
    path('logout/',views.Logout),
    path('upload',views.Upload)
]