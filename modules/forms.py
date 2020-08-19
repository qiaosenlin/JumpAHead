from django import forms
from .models import Task


class checkCompleteTaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = [
        'checkComplete', # 'description'
        ]



        #self.fields['description'].initial = self.instance.description
