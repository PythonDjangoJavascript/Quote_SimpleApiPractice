from django.urls import path
from . import views

urlpatterns = [
    path('quotes/', views.QuoteListCreateAPIView.as_view(), name='quot-list'),

]
