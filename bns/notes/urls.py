from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="NotesHome"),
    path("about/", views.about, name="AboutUs"),
    path("contact/", views.contact, name="ContactUs"),
    path("viewNotes/", views.viewNotes, name="viewNotes"),
]