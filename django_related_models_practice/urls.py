from django.urls import path
import app.views
from django.contrib import admin

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", app.views.album_list, name="album_list"),
    path("album/<id>", app.views.album_details, name="album_details"),
    path("album/<id>/songs", app.views.new_song, name="new_song"),
]
