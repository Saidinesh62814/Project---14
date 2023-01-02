from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':6613,'b':225,}
    return render(request,'conditions.html',d)

