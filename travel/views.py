
from django.shortcuts import get_object_or_404, render,redirect
from django.db.models import Q
from travel.models import Travel
from .forms import NewTravel, TravelParameters

# Create your views here.
def travel(request):
    Form = TravelParameters
    travel = Travel.objects.all()
    return render(request, 'travel/travel.html',{'travel':travel,'Form':Form})

def travel_filter(request):
    Form = TravelParameters
    start = request.GET.get('S')
    destonation = request.GET.get('D')
    travel = Travel.objects.filter(Q(Start__icontains=start,Destonation__icontains=destonation))
    return render(request, 'travel/travel.html',{'travel':travel,'Form':Form})


def travel_detail(request,pk):
    travel_detail = get_object_or_404(Travel, pk=pk)
    return render(request, 'travel/travel_detail.html',{'travel_detail':travel_detail})


def travel_new(request):
    if request.method == "POST":
        form = NewTravel(request.POST)
        if form.is_valid():
            travel = form.save(commit=False)
            travel.save()
            return redirect('travel')
    else:
        form = NewTravel()
    return render(request, 'travel/travel_new.html', {'form': form})

