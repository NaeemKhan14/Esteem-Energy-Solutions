from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Home.models import room, plugs , plug_electricity_consumption, energy_generation, energy_mode, battery,power_transaction, power_generation
import requests



class BackgroundClass:
    @staticmethod
    def test_func():
        print("HIIIIIIIIIIII")
    
    @staticmethod
    def power_allot_func():
        #check power mode
        #Total power consumption by house 
        # Do according transaction 
        print("lol")


class HomePage(TemplateView):
    template_name = 'home/index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {"Room": room.objects.all()})

    def post(self, request, *args, **kwargs):
        if 'remove_room' in request.POST:
            room.objects.filter(room_no=request.POST.get('room_no')).delete()
        else:
            room.objects.create(room_name=request.POST.get('name'))

        return redirect('homepage')


class EnergyGeneration(TemplateView):
    template_name = 'home/energy.html'

    def get(self, request, *args, **kwargs):
        ## Not secure but working solution 
        type_data = request.GET.get('type_data')
        
        if type_data != None:
           energy_mode.objects.all().delete()
           energy_mode.objects.create(mode_id=type_data)

        # Sending current mode active  
        return render(request, self.template_name, {"Energy_mode" : energy_mode.objects.all()})


class RoomPage(TemplateView):
    template_name = 'home/room.html'

    def get(self, request, *args, **kwargs):
        # Try and except for smart plugs in the room
        try:
            plugs_in_room = plugs.objects.filter(room_no=kwargs["room_no"])
        except plugs.DoesNotExist:
            plugs_in_room = []

        # Forces it to an array if their is only 1 result
        if not hasattr(plugs_in_room, '__iter__'):
            plugs_in_room = [plugs_in_room]

        consumption = []
        available_devices = []
        #@Naeem the ip address must come from the database 
        response = requests.get("http://127.0.0.1:5000/api/alldevicesconsumption/").json()

        for index in range(len(response)):
            available_devices.append(response[index]['DeviceName'])

        room_devices = []
        for plug in plugs_in_room:
            #@Naeem the ip address must come from the database 
            api_devices = requests.get("http://127.0.0.1:5000/api/energyconsumption/" + plug.plug_name).json()
            consumption.append(api_devices)
            room_devices.append(plug.plug_name)

        m = [x for x in available_devices if x not in room_devices]
        print(m)
        return render(request, self.template_name, {"Room": room.objects.all(),
                                                    "Room_in": room.objects.get(room_no=kwargs["room_no"]),
                                                    "Plugs": plugs_in_room, "Consumption": consumption},
                      )


    def post(self, request, *args, **kwargs):

        if 'change_status' in request.POST:
            #@Naeem the ip address must come from the database 
            requests.get("http://127.0.0.1:5000/api/changestatus/" + request.POST['change_status'])

        if 'add_device' in request.POST:
            plugs.objects.create(plug_name=request.POST.get('plug_name'),
                                 plug_model_name=request.POST.get('plug_model_name'),
                                 ip_address=request.POST.get('ip_address'),
                                 room_no=room.objects.get(room_no=request.POST['room_no']))
        if 'remove_device' in request.POST:
            plugs.objects.filter(plug_no=request.POST.get('plug_no')).delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
