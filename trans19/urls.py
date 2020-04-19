from django.urls import path

from trans19 import views

urlpatterns = [
    path('', views.Login.as_view(), name="Login"),
    path('homepage/', views.Homepage.as_view(), name="Homepage"),
    path('patient/<int:patient_pk>', views.PatientDetails.as_view(),
         name="patient-details")
]
