from django.shortcuts import render
from django.http import HttpResponse
from .models import registertion

# Create your views here.
def home(request):
    return render(request,'home.html')

def reg(request):
    if request.method=='POST':
        firstname=request.POST['fname']
        lastname=request.POST['lname']
        email=request.POST['email']
        companyname=request.POST['compname'] 
        companyurl=request.POST['copmurl']
        companysize=request.POST['compsize']
        phone=request.POST['pnum']
        Organisation=request.POST['describe']
        Comments=request.POST['comments']
        
        
        obj=registertion()
        obj.Firstname = firstname
        obj.Lastname= lastname
        obj.Email= email
        obj.Companyname= companyname
        obj.Companysize = companysize
        obj.Companyurl = companyurl
        obj.Phone = phone
        obj.organisation= Organisation
        obj.comments = Comments
        obj.save()
    
    else:
        return render(request,'register.html')
    


