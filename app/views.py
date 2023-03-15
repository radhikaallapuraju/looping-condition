from django.shortcuts import render

# Create your views here.
def sample(request):
    d={'name':'RADHIKA'}
    return render(request,'looping condition.html',d)
