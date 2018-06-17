from django.shortcuts import render, redirect
from .forms import InfoForm
from .models import Info

# Create your views here.


def home(request):
    if request.method == 'POST':
        form = InfoForm(request.POST)
        if form.is_valid():
            # name = request.POST['name']
            # Info.objects.create(name=name)
            form.save()
            return redirect('/') #Use redirect to avoid posting same data on page refresh
    form = InfoForm()
    info_list = Info.objects.all()
    return render(request, 'app1/index.html', {'form': form, 'info_list': info_list})
