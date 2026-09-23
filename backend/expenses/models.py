from django.db import models


class ExpenseCategory(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.name


class VatOption(models.Model):
    name = models.CharField(max_length=5, unique=True)

    def __str__(self):
        return self.name


class Expense(models.Model):
    expense_id = models.AutoField(primary_key=True)
    date = models.DateField()
    expense_category = models.ForeignKey(
        ExpenseCategory,
        on_delete=models.PROTECT,
        related_name='expenses'
    )
    description = models.TextField()
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    vat_inclusive = models.ForeignKey(
        VatOption,
        on_delete=models.PROTECT,
        related_name='expenses'
    )

    def __str__(self):
        return f"{self.expense_id} - {self.description}"