from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from .serializers import ExpenseSerializer, GroupSerializer
from .models import Expense, Group
from rest_framework import generics
from acc.authentication import CustomUserAuthentication
# Create your views here.


class CreateExpenseView(generics.CreateAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [CustomUserAuthentication, ]

    

class CreateGroupView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    authentication_classes = [CustomUserAuthentication, ]


class ExpenseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Expense.objects.all()
    serializer_class = ExpenseSerializer
    authentication_classes = [CustomUserAuthentication, ]
