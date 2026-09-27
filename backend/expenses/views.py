from rest_framework import viewsets

from .models import Expense, ExpenseCategory, VatOption
from .serializers import (
    ExpenseSerializer,
    ExpenseCategorySerializer,
    VatOptionSerializer,
)


class ExpenseCategoryViewSet(viewsets.ModelViewSet):
    queryset = ExpenseCategory.objects.all()
    serializer_class = ExpenseCategorySerializer


class VatOptionViewSet(viewsets.ModelViewSet):
    queryset = VatOption.objects.all()
    serializer_class = VatOptionSerializer


class ExpenseViewSet(viewsets.ModelViewSet):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer