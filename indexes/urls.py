from django.urls import path
from .views import DAX, NYSEComposite

urlpatterns = [
    path('dax/', DAX.as_view()),
    path('nyse/', NYSEComposite.as_view())
]
