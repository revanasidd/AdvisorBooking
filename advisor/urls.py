from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('booking',views.Bookingview,basename='Bookingdetails')
router.register('advisor',views.AdvisorViwset,basename='advisordetails')
urlpatterns = [
	path('',include(router.urls)),
]
