from django.shortcuts import render

# Create your views here.
def bootstrap(request):
    return render(request,'bootstrap.html')

def bootstrap2(request):
    return render(request,'bootstrap2.html')

def about1(request):
    return render(request,'about1.html')

def about2(request):
    return render(request,'about2.html')

def card(request):
    return render(request,'card.html')

def about3(request):
    return render(request,'about3.html')