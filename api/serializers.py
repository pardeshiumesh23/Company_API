from rest_framework import serializers
from api.models import Company,Employee
#create serializers
#serializer for Company api
class CompanySerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField() 
    class Meta:
        model=Company
        fields="__all__"
        
#serializer for Employee api
class EmployeeSerializers(serializers.HyperlinkedModelSerializer):
    id=serializers.ReadOnlyField()
    class Meta:
        model=Employee
        fields="__all__"