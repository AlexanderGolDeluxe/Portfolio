from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index_page"),
    path("<language>/", views.index, name="index_page"),
    path("refresh_form", views.refresh_form, name="refresh_form")
]
