from rest_framework import serializers
from .models import Company, Employee


class CompanySerializers(serializers.ModelSerializer):
    company_id = serializers.ReadOnlyField()
    class Meta:
        model = Company
        fields = "__all__"

class EmployeeSerializers(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()
    class Meta:
        model = Employee
        fields = "__all__"