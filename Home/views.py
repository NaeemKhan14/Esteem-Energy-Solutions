from django.shortcuts import render
from django.views.generic import TemplateView
from Home.models import room,plugs


class HomePage(TemplateView):
    template_name = 'home/index.html'
        
    def get(self, request, *args, **kwargs):
        Room = room.objects.all()
        return render(request, self.template_name, {"Room":Room})
    

class EnergyGeneration(TemplateView):
    template_name = 'home/energy.html'
    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})


class RoomPage(TemplateView):
    template_name = 'home/room.html'

    def get(self, request, *args, **kwargs):
        Room_no = request.GET["room_no"]
        Room_in = room.objects.get(room_no=Room_no)
        Room = room.objects.all()
        Plugs_in_room = plugs.objects.get(room_no=Room_no)

        # Forces it to an array if their is only 1 result
        if not hasattr(Plugs_in_room, '__iter__'):
            Plugs_in_room = [Plugs_in_room]

        return render(request, self.template_name, {"Room":Room,"Room_in":Room_in,"Plugs":Plugs_in_room})

