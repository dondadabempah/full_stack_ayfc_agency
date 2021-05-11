from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.


# Homepage endpoint
def main(request):
    return HttpResponse("Hello")

