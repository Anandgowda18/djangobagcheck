from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
import random
def red_green(request):
    x = random.random()
    if x > 0.3:
        return render(request,'index_green.html')
    else:
        return render(request,'index_red.html')