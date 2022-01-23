
from django import views
from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from .forms import surveyform
# Create your views here.

def Surveyviewfun(request):
    return render(request,"surveyhtml.html")

class mainclassview(View):
    def get(self,request):
        forms = surveyform()
        return render(request,"survey.html",{
            "forms":forms
        })

    def post(self,request):
        form = surveyform(request.POST)
        if form.is_valid :
            form.save()
            return HttpResponse("Thanks for you feedbacsk")
        return render(request, 'survey.html')


class Surveyview(View):
    def get(request):
        forms = surveyform()
        return render(request,"survey.html",{
            "forms":forms
        })

    def post(request):
        print("priendtedfsakljlskjdks,")
        return render(request, 'survey.html')