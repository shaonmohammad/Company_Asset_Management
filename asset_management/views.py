# asset_management/views.py

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import AssetForm
from .models import Device, DeviceLog, Employee
from django.utils import timezone


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('home')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})


def add_asset(request):
    if request.method == 'POST':
        form = AssetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('asset_list')
    else:
        form = AssetForm()
    return render(request, 'asset_management/add_asset.html', {'form': form})


def check_out_device(request, device_id, employee_id):
    device = Device.objects.get(id=device_id)
    employee = Employee.objects.get(id=employee_id)

    device.checked_out = True
    device.save()

    log_entry = DeviceLog(device=device, employee=employee,
                          checked_out_date=timezone.now())
    log_entry.save()

    return redirect('device_list')
