from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from accountapp.models import HelloWorld


# Create your views here.

def hello_world(request):
    hello_world_list = HelloWorld.objects.all()

    if request.method == "POST":
        tmp = request.POST.get('hello_world_input')

        new_hello_world = HelloWorld()
        new_hello_world.text = tmp
        new_hello_world.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))
    else:
        return render(request, 'accountapp/hello_world.html', context={'hello_world_list': hello_world_list})
