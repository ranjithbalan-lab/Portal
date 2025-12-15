from django.urls import path
from . import views
# Add this line:
app_name = 'tickets'
urlpatterns = [
    path("", views.index, name='home'),
    path("create/", views.create, name='create'),
    # path("/store/", views.store, name='store'),
    # path("/<int:id>/edit/", views.edit, name='edit'),
    # path("/<int:id>/update/", views.update, name='update'),
    # path("/<int:id>/delete/", views.delete, name='delete'),
]
