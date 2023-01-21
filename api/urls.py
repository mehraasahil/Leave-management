
# Create your tests here.
from django.contrib import admin
from django.urls import path,include
from api.views import UserViewSet,AddLeaveViewSet,EmpidViewset
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'user', UserViewSet)
router.register(r'addleave', AddLeaveViewSet)
router.register(r'empid',EmpidViewset)

urlpatterns = [
    
    path('',include(router.urls)) 
    
    
]