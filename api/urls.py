from django.contrib import admin
from django.urls import path,include
from api.views import CompanyViewSet,EmployeeViewSet
from rest_framework import routers

router=routers.DefaultRouter()#Routers are used with Viewset for auto config the urls
router.register(r'companies',CompanyViewSet)  #this is url where you need to hit request
router.register(r'employees',EmployeeViewSet)

urlpatterns = [
    path('',include(router.urls)) #mapped the url with router
]   
