from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import DayViewSet, ExpenseViewSet

router = DefaultRouter()
router.register('days', DayViewSet, basename='days')
router.register('expenses', ExpenseViewSet, basename='expenses')

urlpatterns = [
    path('expense-api/', include(router.urls)),
]
