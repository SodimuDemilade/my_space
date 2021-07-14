from django.urls import path
from templates_app import views

# SET THE NAMESPACE!
app_name = 'templates_app'

urlpatterns=[
    path('relative/',views.relative,name='relative'),
    path('other/',views.other,name='other'),
]
