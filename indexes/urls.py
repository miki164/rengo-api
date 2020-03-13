from django.urls import path
from .views import *

urlpatterns = [
    path('dax/', DAX.as_view()),
    path('nyse/', NYSEComposite.as_view()),
    path('nasdaq/', NasdaqComposite.as_view()),
    path('dow30/', DowJonesIndustrialAverage.as_view()),
    path('sandp500/', SAndP500.as_view()),
]
