from django.contrib import admin
from api.models import Company,Employee
# Register your models here.

class CompanyAdmin(admin.ModelAdmin): #this is to display employee in proper way in django admin section after login
    list_display=('name','location','type') #pass the column name here
    search_fields=('name',) #to search company by its name  

class EmployeeAdmin(admin.ModelAdmin):
    list_display=('name','email','company')
    list_filter=('company',) #filter employees based on the company
admin.site.register(Company,CompanyAdmin)
admin.site.register(Employee,EmployeeAdmin)