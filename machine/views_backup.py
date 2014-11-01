from django.shortcuts import render, HttpResponseRedirect, render_to_response
from django.core.urlresolvers import reverse
from django.contrib.auth.models import User

from django.views.generic.list import ListView
from django.utils import timezone

from machine.models import Controller
from machine.forms import DeviceForm
from django.views.decorators.csrf import csrf_exempt

class ControllerListView(ListView):

    model = Controller

    def get_context_data(self, **kwargs):
        context = super(ControllerListView, self).get_context_data(**kwargs)
        context['now'] = timezone.now()
        return context

    def get_queryset(self):
        """Override get_querset so we can filter on request.user """
        return Controller.objects.filter(user=self.request.user)


def add_machine(request):
    if request.method == 'GET':
        form = DeviceForm()
    else:
        # A POST request: Handle Form Upload
        form = DeviceForm(request.POST) # Bind data from request.POST into a PostForm

        # If data is valid, proceeds to create a new post and redirect the user
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return HttpResponseRedirect(reverse('device-list'))
        else:
            print 'invalid form data'
    return render(request, 'machine/add_machine.html', {
        'form': form,
    })

import json

@csrf_exempt
def add_machine_through_phone(request):
    if request.method == 'POST':

        data = request.body
        data = json.loads(data)
        print data
        username = data['username']
        if not username_present(username):
            # username was incorrect
            return render(request, 'machine/add_machine_through_phone.html', {
                'result':'incorrect username/password',
                })

        password = data['password']
        user = User.objects.get(username = username)
        if user.check_password(password):
            # both username and password check out
            new_device = Device(user = user,
                                name = data['name'],
                                field_1 =  data['field_1'],
                                field_2 = data['field_2'])
            new_device.save()
            return render(request, 'machine/add_machine_through_phone.html', {
                'result':'successfully added device',
                })


        else:
            # password was incorrect
            return render(request, 'machine/add_machine_through_phone.html', {
                'result':'incorrect username/password',
                })

def username_present(username):
    if User.objects.filter(username=username).count():
        return True

    return False

def deviceData(request, data_id=1):
    return render_to_response('index.html',
                        {'data': Device.objects.get(id=data_id)})


import os
from aquabrim_project.settings import BASE_DIR


DATA_STORAGE_FOLDER = os.path.join(BASE_DIR, 'uploaded_files_from_board')
DATA_STORAGE_FILENAME = os.path.join(DATA_STORAGE_FOLDER, 'data_dump')

@csrf_exempt
def collect_data_from_device(request):
    if request.method == 'POST':

        data = request.body
        data = json.loads(data)
        print data

        f = open(DATA_STORAGE_FILENAME, 'a+')
        string_to_write = '<data>%s</data>' % data
        f.write(string_to_write + '\n')
        f.close()

        return render(request, 'machine/data_received_from_board.html', {
            'result':'successfully uploaded data to server...',
        })

