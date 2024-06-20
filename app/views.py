from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework.pagination import PageNumberPagination
from .models import Day, Expense
from .serializers import DaySerializer, ExpenseSerializer
from rest_framework.authentication import SessionAuthentication, BasicAuthentication


class DayViewSet(viewsets.ModelViewSet):
    """This view is for weekdays"""

    queryset = Day.objects.all()
    serializer_class = DaySerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]


class ExpenseViewSet(viewsets.ModelViewSet):
    """This view is for expenses"""

    serializer_class = ExpenseSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = PageNumberPagination
    authentication_classes = [SessionAuthentication, BasicAuthentication]

    def get_queryset(self):
        return Expense.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
