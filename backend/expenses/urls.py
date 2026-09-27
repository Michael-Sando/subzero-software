from rest_framework.routers import DefaultRouter

from .views import (
    ExpenseViewSet,
    ExpenseCategoryViewSet,
    VatOptionViewSet,
)


router = DefaultRouter()

router.register(
    r'expenses',
    ExpenseViewSet,
    basename='expense'
)

router.register(
    r'expense-categories',
    ExpenseCategoryViewSet,
    basename='expense-category'
)

router.register(
    r'vat-options',
    VatOptionViewSet,
    basename='vat-option'
)

urlpatterns = router.urls