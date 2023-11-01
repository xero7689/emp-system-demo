from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import Department, Role, Employee, User


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Role)
class RoleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'active')
    search_fields = ('title', 'slug')
    prepopulated_fields = {'slug': ('title',)}


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('user', 'department', 'service_status', 'date_of_hire')
    search_fields = ('user', 'department', 'role')


class EmployeeInline(admin.StackedInline):
    model = Employee
    can_delete = True
    verbose_name_plural = "Employ Information"
    fk_name = 'user'


@admin.register(User)
class CustomUserAdmin(UserAdmin):
    inlines = [EmployeeInline]
    fieldsets = (*UserAdmin.fieldsets, ('Additional Info',
                 {'fields': ('phone_number', 'address')}))

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)
