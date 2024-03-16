from django.urls import path
from . import views

urlpatterns = [
    path('reminder/<int:id>', views.reminder, name='reminder'),
    path('reminder', views.reminder, name='reminder_P')
]
