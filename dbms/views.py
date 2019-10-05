from django.shortcuts import render
from django.http import HttpResponse
from dbms.models import booking

# Create your views here.
def index(request):
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin = request.POST.get('pin', '')
        bks = booking(fname=fname,lname=lname,email=email,city=city,state=state,pin=pin)
        bks.save()
        print("hi")
    else:
        print('hello')
    return render(request,'dbms\index.html')
def submit(request):
    return render(request,'dbms\submitted.html')
def adminp(request):
    x=booking.objects.all()
    print(x)
    params={'pro': x}
    return render(request,'dbms/adminpanel.html',params)
    