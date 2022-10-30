
from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from app import views as tropikoViews



urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', tropikoViews.index),
    path('fruits', tropikoViews.service),
    path('service', tropikoViews.service),
    path('contact', tropikoViews.contact),

]
