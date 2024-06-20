from rest_framework import serializers
from .models import Day, Expense


class DaySerializer(serializers.ModelSerializer):
    """serializer for days of the week"""
    class Meta:
        model = Day
        fields = ['id', 'name', 'created']


class ExpenseSerializer(serializers.ModelSerializer):
    """Serializer for expense model"""
    class Meta:
        model = Expense
        fields = ['id', 'user', 'title', 'description', 'amount', 'day', 'date']
        read_only_fields = ['user']
