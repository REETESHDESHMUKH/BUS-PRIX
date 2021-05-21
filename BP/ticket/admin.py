from django.contrib import admin

# Register your models here.
from .models import Bus, Passengers, Bus_stops, Route, Schedules, Bus_ticket, Help

admin.site.register(Bus)
admin.site.register(Passengers)
admin.site.register(Bus_stops)
admin.site.register(Route)
admin.site.register(Schedules)
admin.site.register(Bus_ticket)
admin.site.register(Help)