# Write all the api endpoints (routes) in this file
from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes, name="routes"), # Home Page
    path('notes/', views.getNotes, name="notes"), # ALL Notes
    path('notes/create/', views.createNote, name ="createNote") , # Create Note
    path('notes/<str:pk>/update/', views.updateNote, name="updateNote"),  # Update Note
    path('notes/<str:pk>/delete/', views.deleteNote, name="deleteNote"),  # Delete Note
    path('notes/<str:pk>/', views.getSingleNote, name="singleNote"), # Single Note
]