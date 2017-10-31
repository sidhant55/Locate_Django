# from django.shortcuts import render
from .models import Locator
from .serializers import LocatorSerializer
# from rest_framework.views import APIView
from rest_framework import status, generics, permissions
from rest_framework.response import Response
# from rest_framework.request import Request
from rest_framework.decorators import api_view
# from django.http import JsonResponse
# from django.http import QueryDict
from django.shortcuts import render,redirect
from .forms import dataform
# Create your views here

@api_view(['GET','POST'])
def LocatorSerialView(request):
    # print(request.GET['scu_id'], request.GET['lat'], request.GET['lon'])
    # scu_id = request.GET['scu_id']
    # lat = request.GET['lat']
    # lon = request.GET['lon']
    # print(request.data)
    # js = "{\"scu_id\":[\'"+str(scu_id)+"\'],\"latitude\":[\'"+str(lat)+"\'],\"longitude\":[\'"+str(lon)+"\']}"
    js = {'scu_id': scu_id, 'latitude': lat, 'longitude': lon}
    # js = QueryDict(js)
    print(js)
    serial = LocatorSerializer(data=js)
    if serial.is_valid():
        serial.save()
        return Response(status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET','POST'])
def LocatorFetch(request, scu_id = None):
    try:
        obj = Locator.objects.filter(scu_id=scu_id)[:1]
        # obj = Locator.objects.all()
        print(obj)
    except Locator.DoesNotExist:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial = LocatorSerializer(obj, many=True)
    return Response(serial.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def AllScu(request):
    try:
        obj = Locator.objects.all()
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)
    serial = LocatorSerializer(obj, many=True)
    ar =[]
    for i in range(len(serial.data)):
        ar.append((serial.data)[i]['scu_id'])
    ar =set(ar)
    return Response(ar, status=status.HTTP_200_OK)


def mapview(request, id=None):
    return render(request, "map.html", {'id':id})

@api_view(['GET'])
def timeview(request,scu_id=None,start=None, end=None):
    print
    try:
        obj = Locator.objects.filter(scu_id=scu_id,created__range=[start,end])

    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    serial =LocatorSerializer(obj, many=True)

    return Response(serial.data, status=status.HTTP_200_OK)


def indexview(request):
    form = dataform(request.POST or None)
    if form.is_valid():
        scu_id = form.cleaned_data['scu_id']
        startdate = form.cleaned_data['startdate']
        starttime = form.cleaned_data['starttime']
        enddate = form.cleaned_data['enddate']
        endtime = form.cleaned_data['endtime']
        if starttime != "":
            start = startdate+'T'+starttime
        else:
            start = startdate
        if endtime != "":
            end =enddate+'T'+endtime
        else:
            end = enddate
        return redirect('/map/'+scu_id+'/'+start+'/'+end) # change according to URL
        # return r(request, "polyline.html", {'scu_id':scu_id,'start':start, 'end':end})
    return render(request, "index.html", {'form':form})

def polyview(request, scu_id=None, start = None, end =None):
    return render(request, "polyline.html", {'scu_id':scu_id, 'start':start, 'end':end })