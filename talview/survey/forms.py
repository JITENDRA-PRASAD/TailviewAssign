from django import forms
from .models import Surveymodel

class surveyform(forms.ModelForm):
    class Meta:
        model = Surveymodel
        fields = "__all__"
        labels = {
            "Role":"Which option best describe your current role ?",
            "friendshare" : "Would you recommend this application to a friend?",
            "features" : "Which is your favorite feature of the application?",
            "improve" : "What would you like to see improved?",
            "comments" : "Any comment or suggestions?"
        }