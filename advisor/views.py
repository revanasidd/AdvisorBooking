from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets

from .models import AdvisorModel
from .serialazier import AdvisorModelSerializer,BookingModelSerializer

# Create your views here.
class Advisor(viewsets.ViewSet):
    def list(self,request):
        adv = AdvisorModel.objects.all()
        serializer = BookingModelSerializer(adv,many=True)
        return Response(serializer.data)

class AdvisorViwset(viewsets.ViewSet):
    def list(self,request):
        adv = AdvisorModel.objects.all()
        serializer = AdvisorModelSerializer(adv,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk):
        id=pk
        if id is not None:
            adv = AdvisorModel.objects.get(id=id)
            serializer = AdvisorModelSerializer(adv)
            return Response(serializer.data)
    def create(self,request):
        serializer = AdvisorModelSerializer(data=request.data)
        if serializer.is_valid():
            advuser = serializer.save()
            return Response({'advname':advuser.advname,'image_url':advuser.image},status=status.HTTP_201_CREATED)
        return Response('Invalid',status=status.HTTP_400_BAD_REQUEST)

class Bookingview(viewsets.ViewSet):
    def list(self,request):
        adv = AdvisorModel.objects.all()
        serializer = BookingModelSerializer(adv,many=True)
        return Response(serializer.data)

    def create(self,request):
        serializer = BookingModelSerializer(data=request.data)
        if serializer.is_valid():
            advuser = serializer.save()
            return Response({'booking_id':advuser.id,'bookingdate':advuser.bookingdate},status=status.HTTP_201_CREATED)
        return Response('Invalid',status=status.HTTP_400_BAD_REQUEST)
