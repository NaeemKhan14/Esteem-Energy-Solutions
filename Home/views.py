from django.contrib.sites import requests
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Home.models import room, plugs
import requests




class TestClass:

    @staticmethod
    def test_func():
        print("HIIIIIIIIIIII")


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
        return render(request, self.template_name)


def change_status_fn(device):
    change_status_url = "http://127.0.0.1:5000/api/changestatus/" + device
    change_status_response = requests.get(change_status_url)







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

        devices = []
        consumption = []

        for d in plugs_in_room:
            devices.append(d.plug_name)
        print(devices)

        def get_consumption(device):
            get_consumption_url = "http://127.0.0.1:5000/api/energyconsumption/" + device
            get_consumption_response = requests.get(get_consumption_url)
            # print("Consumption of " + device + " is " + str(get_consumption_response.json()))
            consumption.append(get_consumption_response.json())

        def live_consumption():
            for i in range(len(devices)):
                get_consumption(devices[i])
            print(consumption)
            return consumption

        print("test")
        live_consumption()


        return render(request, self.template_name, {"Room": room.objects.all(),
                                                    "Room_in": room.objects.get(room_no=kwargs["room_no"]),
                                                    "Plugs": plugs_in_room, "Consumption": consumption},


                      )

    def post(self, request, *args, **kwargs):
        room_no = request.POST.get('room_no')

        if 'change_status' in request.POST:
            change_status_fn(request.POST['change_status'])

        if 'add_device' in request.POST:
            plugs.objects.create(plug_name=request.POST.get('plug_name'),
                                 plug_model_name=request.POST.get('plug_model_name'),
                                 ip_address=request.POST.get('ip_address'),
                                 room_no=room.objects.get(room_no=room_no))
        if 'remove_device' in request.POST:
            plugs.objects.filter(plug_no=request.POST.get('plug_no')).delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
