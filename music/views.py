#from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
# Create your views here.
from django.http import HttpResponse
from . models import Categories
from django.template import loader

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
'''from rest_framework import Response, status
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
'''
from .serializer import CategoriesSerializer


def index(request):
    all_categories=Categories.objects.all()
    #template=loader.get_template('music/index.html')
    context={
        'all_categories' : all_categories
    }
    return render(request, 'music/index.html', context)

def detail(request,categories_id):
    cat = get_object_or_404(Categories, pk=categories_id)
    return render(request, 'music/detail.html', {'cat': cat})
    #return HttpResponse("You're looking at %s." % categories_id)

def all(request):
    all_categories=Categories.objects.all()
    all_products=[]
    for cat in all_categories:
        for prod in cat.product_set.all():
            all_products.append(prod)

    
    #template=loader.get_template('music/index.html')
    context={
        'all_products' : all_products
        #'all_categories' : all_categories
    }
    return render(request, 'music/all.html', context)


    ####### Can write views as generic views as well...

    ## Now for Django Rest API
    # Should List all Categories or create a new one
class CategoriesList(APIView):
    def get(self,request):
        cat=Categories.objects.all()
        serializer=CategoriesSerializer(cat, many=True)
        return Response(serializer.data)

    def post(self,request):
        pass
        