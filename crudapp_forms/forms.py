from django import forms
from crudapp_forms.models import employee
class employeeforms(forms.ModelForm):
    class Meta:
        model = employee
        fields = '__all__'