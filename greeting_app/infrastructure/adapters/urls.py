from django.urls import path
from greeting_app.infrastructure.adapters.views import GreetPersonView

urlpatterns = [
    path('saludar/', GreetPersonView.as_view(), name='greet-person'),
]