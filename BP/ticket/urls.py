from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="TicketHome"),
    path("help/", views.help, name="help"),
    path("login/", views.Login, name="Login"),
    path("signIn/", views.signIn, name="Sign"),
    path("Logout/", views.logout, name="logout"),
    path("list/", views.Bus_list, name="Bus_list"),
    path("Num/", views.num, name="num"),
    path("Usertickets/", views.userticket, name="userticket"),
    path("bookedTicket/<int:psid>", views.bookedTicket, name="bookedTicket"),
    path("ticketBooking/<int:myid>", views.ticketBooking, name="ticketBooking"),
]