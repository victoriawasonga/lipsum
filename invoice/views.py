from django.shortcuts import render

def home(request):
    #return render(request,'_partials/base.html')
    return render(request,'invoice/dashboard.html')