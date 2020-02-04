from django.shortcuts import render,redirect
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
        Room = room.objects.all()
        Room_no = request.GET["room_no"]
        Room_in = room.objects.get(room_no=Room_no)
        
        # Try and except for smart plugs in the room
        try:
            Plugs_in_room = plugs.objects.filter(room_no=Room_no)
        except plugs.DoesNotExist:
            Plugs_in_room = []

        # Forces it to an array if their is only 1 result
        if not hasattr(Plugs_in_room, '__iter__'):
            Plugs_in_room = [Plugs_in_room]

        return render(request, self.template_name, {"Room":Room,"Room_in":Room_in,"Plugs":Plugs_in_room})

class Rooms(TemplateView):
    template_name = 'home/index.html'

    def post(self, request, *args, **kwargs):
        if(request.POST.get('type') == 'remove'):
           room_no = request.POST.get('room_no')
           room.objects.filter(room_no=room_no).delete()
        else:   
           room_name = request.POST.get('name')
           room.objects.create(room_name=room_name)
        
        return redirect('/')

class Plugs(TemplateView):
    template_name = 'home/room.html'

    def post(self, request, *args, **kwargs):

        room_no = request.POST.get('room_no')

        if(request.POST.get('type') == 'add'):
           plug_model_name = request.POST.get('plug_model_name')
           plug_name = request.POST.get('plug_name')
           turn_on = request.POST.get('turn_on')
           turn_off = request.POST.get('turn_off')
           current_status = request.POST.get('current_status')
           Room_in = room.objects.get(room_no=room_no)

           plugs.objects.create(plug_name=plug_name,plug_model_name=plug_model_name,turn_on=turn_on,
           turn_off=turn_off,current_status=current_status,room_no=Room_in)

        else:   
           plug_no = request.POST.get('plug_no')
           plugs.objects.filter(plug_no=plug_no).delete()

        return redirect('/room?room_no='+room_no)


        
