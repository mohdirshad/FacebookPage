from django.conf.urls import url, include
from django.contrib import admin
import views

urlpatterns = [
    url(r'^',views.Home.as_view(),),
    url(r'update/^',views.UpdatePage.as_view(),),

]
