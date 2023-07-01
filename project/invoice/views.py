from django.shortcuts import render, get_object_or_404
from .models import products, seller,buyer
from .forms import Newuser
import datetime


# Create your views here.
def index(request):
    global slr,buy
    pro = products.objects.all()
    slr = seller.objects.all()
    buy = buyer.objects.all()
    return render(request, 'index.html', {'products': pro, 'seller': slr})


def user(request):
    form=Newuser()
    if request.method=='POST':
        form = Newuser(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return render(request,'pdf.html',{'seller': slr})

        else:
            return render(request, 'pdf.html')
    return render(request, 'buy.html',{'form':form})


def pdf(request,pk):
    class_to_display = get_object_or_404(buyer, pk=pk)
    slr = seller.objects.all()
    return render(request, 'pdf.html', {'buyer': class_to_display,'seller':slr})

