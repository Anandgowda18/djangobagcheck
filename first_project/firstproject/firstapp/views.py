from django.shortcuts import render
#from django.http import HttpResponse

# Create your views here.
import random
def red_green(request):
    x = random.random()
    if x > 0.5:
        return render(request,'firstproject/templates/index_green.html')
    else:
        return render(request,'firstproject/templates/index_red.html')