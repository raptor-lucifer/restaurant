from .models import Reservation
from django.shortcuts import render 
from .forms import reserveTableForm

# Create your views here.
from .models import Reservation

def reserve_table(request):
    reserve_form=reserveTableForm()

    if request.method== 'POST':
        reserve_form= reserveTableForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
        

    context={'form':reserve_form}


    return render(request, 'reservation/booking.html' , context)

    
