
from django.urls import path,include
from .views import LoginToken, RegisterApi,DetailsUsers
from rest_framework.authtoken import views
from adminApp import views

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register('users',views.DetailsUsers,basename='userdetails')

urlpatterns = [
      path('',include(router.urls)),
      path('register/',RegisterApi.as_view()),
      path('login/',LoginToken.as_view()),
      
]
