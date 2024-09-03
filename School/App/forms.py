from django import forms
from .models import *

class attendanceForm(forms.ModelForm):
    class Meta:
        model=createAttendance
        fields="__all__"

