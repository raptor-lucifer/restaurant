from django.shortcuts import render
from .models import Chef

# Create your views here.
def aboutus(request):
    chef_list=Chef.objects.all()
    context={
        'chef_list':chef_list
    }
    
    return render(request, 'aboutus/aboutus.html', context)