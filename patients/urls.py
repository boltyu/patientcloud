from django.urls import path
from . import views
from .views import IndexView

urlpatterns = [
    path('',IndexView.as_view()),
    path('surgeryapproaches/',views.SurgeryApproachList),
    path('devicetypes/',views.DeviceTypeList),
    path('<str:idnum>/<str:category>/',views.Pic),
    path('<str:idnum>/<str:category>/<str:filename>',views.Picfile),
    path('<str:idnum>/',views.Info)
]