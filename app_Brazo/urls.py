
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('move_servo/', views.move_servo, name='move_servo'),
    path('stream_video/', views.stream_video, name='stream_video')
]


