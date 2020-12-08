from django.urls import path
from . import views

urlpatterns = [
    path('list', views.list_tas, name="list"),
    path('', views.add_ta, name="add"),
    path('coursewise', views.course_wise_talist, name="coursewise"),
]