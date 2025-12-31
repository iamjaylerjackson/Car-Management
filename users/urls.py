from django.urls import path
from .views import ProtectedView
from .views import register

urlpatterns = [
    path('register/', register),
    path('protected/', ProtectedView.as_view(), name='protected'),
]
