from django.urls import path
from . import views
urlpatterns = [
    path('',views.Index),
    path('surgeryapproaches/',views.SurgeryApproachList),
    path('devicetypes/',views.DeviceTypeList),
    path('<str:idnum>/<str:category>/',views.Pic),
    path('<str:idnum>/<str:category>/<str:filename>',views.Picfile),
    path('<str:idnum>/',views.Info)
]