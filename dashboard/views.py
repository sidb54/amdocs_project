from django.shortcuts import render

# Create your views here.

def fr_booking(request):
    return render(request,'dashboard/base.html',{})

def fr_profile(request):
    return render(request,'dashboard/freelancer.html',{})


