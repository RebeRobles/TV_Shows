from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('shows', views.shows, name='shows'),
    path('shows/new', views.new, name='new'),
    path('shows/new_show', views.new_show, name='new-show'),
    path('shows/<show_id>', views.info_show, name='info_show'),
    path('shows/<show_id>/edit', views.edit_show, name='edit_show'),
    path('shows/<show_id>/updated', views.updated_show, name='updated_show'),
    path('shows/<show_id>/delete', views.delete_show, name='delete_show'),
]