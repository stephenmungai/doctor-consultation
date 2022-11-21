from django.urls import path,include
from rest_framework.routers import DefaultRouter

from .views import *

router = DefaultRouter()
router.register('consultation',ConsultationViewset,basename='consult_doctor')

router.register('',DoctorViewSet)
urlpatterns = [
    path('register/',register_doctor,name='register_doctor'),
    path('schedule/',consultation_schedule,name='consultation_schedule'),
    path('prescription/<int:id>/',consultation_details,name='prescription'),
    path('specialities/',specialities),
    path('report/',report)
]+router.urls