from django.shortcuts import render
from django.http import HttpResponse
from dbms.models import booking,approved

# Create your views here.
def index(request):
    if request.method=="POST":
        fname = request.POST.get('fname', '')
        lname = request.POST.get('lname', '')
        email = request.POST.get('email', '')
        city = request.POST.get('city', '')
        state = request.POST.get('state', '')
        pin = request.POST.get('pin', '')
        print(fname,lname,email,city,state,pin)
        bks = booking(fname=fname,lname=lname,email=email,city=city,state=state,pin=pin)
        bks.save()
        print("hi")
    else:
        print('hello')
    return render(request,'dbms\index.html')
def submit(request):
    return render(request,'dbms\submitted.html')
def adminp(request):
    if 'form_rejected' in request.POST and request.method=="POST":
        print("Went into reject")
        p=booking.objects.filter(id=request.POST.get('object_id','')).delete()
        print(p)
    elif 'form_approved' in request.POST and request.method=="POST":
        print("went in approve")
        booking_obj = booking.objects.get(id=request.POST.get('object_id'))
        approved_obj=approved.objects.create(fname=booking_obj.fname,lname=booking_obj.lname,email=booking_obj.email,city=booking_obj.city,state=booking_obj.state,pin=booking_obj.pin)
        booking_obj.delete()
    x=booking.objects.all()
    params={'pro': x}
    return render(request,'dbms/adminpanel.html',params)
