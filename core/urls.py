
from django.contrib import admin
from django.urls import path
from base.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name="homepage"),
    path('person-detail/', get_data, name="person_details"),
    path('delete-person/<int:person_id>', delete_data, name="delete_person"),
    path('update-person/<int:person_id>', update_data, name="update_person")
]
