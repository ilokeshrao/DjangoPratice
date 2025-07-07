from django.shortcuts import render # type: ignore

# Create your views here.
def all_chai(request):
    return render(request,'chai/all_chai.html')
