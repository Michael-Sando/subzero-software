from rest_framework import serializers
from .models import Expense, ExpenseCategory, VatOption


class ExpenseCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = ExpenseCategory
        fields = ['id', 'name']


class VatOptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = VatOption
        fields = ['id', 'name']


class ExpenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Expense
        fields = [
            'expense_id',
            'date',
            'expense_category',
            'description',
            'amount',
            'vat_inclusive',
        ]