from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView

from accountapp.models import HelloWorld


def hello_world(request) :
    if request.method == "POST":

        temp = request.POST.get('input')

        new_data = HelloWorld()
        new_data.text = temp
        new_data.save()

        return HttpResponseRedirect(reverse('accountapp:hello_world'))  # 새로고침 문제 해결

    else:
        data_list = HelloWorld.objects.all()
        return render(request, 'accountapp/hello_world.html',
                      context={'data_list':data_list})


class AccountCreateView(CreateView) :
    model = User
    form_class = UserCreationForm
    success_url = reverse_lazy('accountapp:hello_world')
    template_name = 'accountapp/create.html'




