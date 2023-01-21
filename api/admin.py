from django.contrib import admin
from api.models import User,AddLeave,Empid
# Register your models here.

class UserAdmin(admin.ModelAdmin):
    # list_display=('name','location','type')
    list_display=('name','type')

class AddLeaveAdmin(admin.ModelAdmin):
    # list_display=('name','email','company'
    list_display=['Username']

class EmpidAdmin(admin.ModelAdmin):
    list_display=('name','type')    

# class EmpidAdmin(admin.ModelAdmin):
#     # list_display=('name','location','type')
#     list_display=(



admin.site.register(User,UserAdmin)
admin.site.register(AddLeave,AddLeaveAdmin)
admin.site.register(Empid,EmpidAdmin)


# admin.site.register(Empid,EmpidAdmin)