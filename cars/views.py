from django.shortcuts import get_object_or_404, render
from .models import Car
from django.core.paginator import EmptyPage,PageNotAnInteger,Paginator
# Create your views here.
def Cars(request):
    cars=Car.objects.order_by('-created_date')
    paginator=Paginator(cars,3)
    page=request.GET.get('page')
    paged_cars=paginator.get_page(page)
    data={
        'cars':paged_cars,
        
    }
    return render(request,'cars/cars.html',data)

def Car_details(request,id):
    single_car =get_object_or_404(Car,pk=id)
    data={
        'single_car':single_car,
    }
    return render(request,'cars/car_details.html',data)

def Search(request):
    cars=Car.objects.order_by('-created_date')
    data={
        'cars':cars
    }
    return render(request,'cars/search.html',data)