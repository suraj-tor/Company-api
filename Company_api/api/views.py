from django.shortcuts import render
from .models import Company, Employee
from .serializers import CompanySerializers, EmployeeSerializers
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

# Create your views here.
class CompanyViewsets(viewsets.ModelViewSet):
    """
    This viewset performs CRUD operation on Company table
    also it returns number of employee from a specific company
    """

    queryset = Company.objects.all()
    serializer_class = CompanySerializers

    @action(detail=True, methods=["get"])
    def employees(self, request, pk):
        try:
            company_object = Company.objects.get(pk=pk)
            emp_object = Employee.objects.filter(company=company_object)
            emp_data = EmployeeSerializers(
                emp_object, many=True, context={"request": request}
            ).data
            return Response(emp_data)
        except Exception as e:
            return Response({"message": f"Company not found {e}"})


class EmployeesViewsets(viewsets.ModelViewSet):
    """
    This viewset performs CRUD operation on Employees table
    """

    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializers
