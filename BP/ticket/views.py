from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Passengers,Bus_stops,Schedules,Bus,Route,Bus_ticket,Help
from django.contrib.auth.models import User, auth
# Create your views here.

numi = 0
unip = 0
uni_sch = 0
userpass = 0
def index(request):
    stops = Bus_stops.objects.all()
    alpha = {'stop': stops}

    return render(request,'ticket/index.html',alpha)

def bookedTicket(request,psid):
    global numi, uni_sch, unip, ntic, num
    if request.method == "POST":
        passenger_name = request.POST.get('passenger_name', '')
        image = request.POST.get('image', '')
        contact_no = request.POST.get('contact_no', '')
        city = request.POST.get('city', '')
        email = request.POST.get('email', '')
        date = request.POST.get('date', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')
        num = request.POST.get('num','')


        if password2==password1:
         passenger = Passengers(passenger_name=passenger_name,image=image,contact_no=contact_no,city=city,email=email,password=password1)
         passenger.save()
         schedule = Schedules(route=Route.objects.get(id=psid),time=date)
         schedule.save()
         route1 = Route.objects.get(id=psid)
         b = route1.bus_rou
         num2 = int(num)
         b.number_seats = b.number_seats - (1+num2)
         b.save()
         ticket = Bus_ticket(sch_id=schedule,pass_id=passenger)
         ticket.save()
         uni_sch = schedule
         unip = password1
         ntic = Bus_ticket.objects.filter(id=ticket.id)
         if(num2==0):
             return redirect('/Usertickets')
    numi = int(num) + 1
    hw = {'fin':ntic,'range':range(1,numi),'num':numi}
    return render(request,'ticket/num.html',hw)

def num(request):
    for i in range(numi):
       if request.method == "POST":
         passenger_name = request.POST.get('passenger_name', '')
         image = request.POST.get('image', '')
         contact_no = request.POST.get('contact_no', '')
         city = request.POST.get('city', '')
         email = request.POST.get('email', '')

         passenger = Passengers(passenger_name=passenger_name, image=image, contact_no=contact_no, city=city,
                                email=email, password=unip)
         passenger.save()
         ticket = Bus_ticket(sch_id=uni_sch, pass_id=passenger)
         ticket.save()

    return redirect('/Usertickets')

def userticket(request):
    all_tick = Bus_ticket.objects.filter(pass_id__password__contains = userpass)
    alp = {'tot': all_tick}
    return render(request,'ticket/ticketshowing.html',alp)


def ticketBooking(request,myid):
    route_spec = Route.objects.filter(id=myid)
    ga = {'rou':route_spec}
    return render(request,'ticket/ticketBooking.html',ga)

def Bus_list(request):
    global beta
    if request.method == "POST":
        origin = request.POST.get('origin', '')
        destination = request.POST.get('destination', '')

        route_spec = Route.objects.filter(origin=origin, destination=destination)
        beta = {'list': route_spec}
    return render(request,'ticket/list.html',beta)

def help(request):
    if request.method == "POST":
        Name = request.POST.get('Name','')
        Email = request.POST.get('Email','')
        Message = request.POST.get('Message','')

        seek = Help(Name=Name,Email=Email,Message=Message)
        seek.save()
        messages.info(request, 'your query has been taken')
        return redirect('/')
    return render(request, 'ticket/index.html')

def Login(request):
    global userpass
    if request.method == "POST":
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        userpass = password

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,'invalid credentials')
    return render(request,'ticket/login.html')

def signIn(request):
    if request.method == "POST":
        first = request.POST.get('first', '')
        last = request.POST.get('last', '')
        email = request.POST.get('email', '')
        username = request.POST.get('username', '')
        password1 = request.POST.get('password1', '')
        password2 = request.POST.get('password2', '')


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username taken')
                return redirect('/signIn')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email taken')
                return redirect('/signIn')
            else:
               user = User.objects.create_user(username=username,password=password1,email=email,first_name=first,last_name=last)
               user.save()
        else:
            messages.info(request, 'password not matching')
        return redirect('/')
    else:
        return render(request,'ticket/signin.html')

def logout(request):
    auth.logout(request)
    return redirect('/')