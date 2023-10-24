from django.urls import path
from . import views


urlpatterns = [
    path('CreateExpense/', views.CreateExpenseView.as_view()),
    path('CreateGroup/', views.CreateGroupView.as_view()),
    path('ExpenseDetail/<int:pk>', views.ExpenseDetailView.as_view())
]