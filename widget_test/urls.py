from django.urls import path
from . import views

urlpatterns = [
    path('', views.get_bot_widget,name='get_bot_widget'),
    path('rasa/', views.get_rasa_webchat,name='get_rasa_widget')
]