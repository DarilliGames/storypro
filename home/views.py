from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, "index.html")

def testpage(request):
    return render(request, "error.html")