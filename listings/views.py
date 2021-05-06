from django.shortcuts import render, redirect
from .forms import DashboardForm
from .models import Dashboard

def dashboard_list(request):
    context = {'dashboard_list': Dashboard.objects.all()}
    return render(request, 'dashboard_list.html', context)


def dashboard_form(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = DashboardForm()
        else:
            dashboard = Dashboard.objects.get(pk=id)
            form = DashboardForm(instance=dashboard)
        return render(request, "dashboard_form.html", {'form': form})
    else:
        if id == 0:
            form = DashboardForm(request.POST)
        else:
            dashboard = Dashboard.objects.get(pk=id)
            form = DashboardForm(request.POST,instance= dashboard)
        if form.is_valid():
            form.save()
        return redirect('/dashboard/list')


def dashboard_delete(request,id):
    dashboard = Dashboard.objects.get(pk=id)
    dashboard.delete()
    return redirect('/dashboard/list')