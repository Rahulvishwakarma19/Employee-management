from django.contrib import admin
from django.urls import path,include
from .views import *

urlpatterns = [
    path('home/',emp_home),
    path('add-emp/',add_emp),
    path('delete-emp/<int:e_id>',delete_emp),
    path('update-emp/<int:e_id>',update_emp),
    path('do-update-emp/<int:e_id>',do_update_emp),
    path('testimonials/',testimonials)
   
]