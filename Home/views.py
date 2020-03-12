from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from Home.models import room, plugs , plug_electricity_consumption, energy_generation, energy_mode, battery,power_transaction, power_generation


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
        #plugs.objects.create(type_data)
        energy_mode.objects.all().delete()
        if type_data != None:
           energy_mode.objects.create(mode_id=type_data)

        print(energy_mode.objects.all())

        # Type_data for 
        return render(request, self.template_name)


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

        return render(request, self.template_name, {"Room": room.objects.all(),
                                                    "Room_in": room.objects.get(room_no=kwargs["room_no"]),
                                                    "Plugs": plugs_in_room})

    def post(self, request, *args, **kwargs):
        room_no = request.POST.get('room_no')

        if 'add_device' in request.POST:
            plugs.objects.create(plug_name=request.POST.get('plug_name'),
                                 plug_model_name=request.POST.get('plug_model_name'),
                                 ip_address=request.POST.get('ip_address'),
                                 room_no=room.objects.get(room_no=room_no))
        if 'remove_device' in request.POST:
            plugs.objects.filter(plug_no=request.POST.get('plug_no')).delete()

        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))


    

    
    
       



