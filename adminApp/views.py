from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework import viewsets

from advisor.serialazier import AdvisorModelSerializer
from django.contrib.auth.models import User
from .serializer import RegisterSerializer,LoginSerializer,UserModelSerializer

#Register API
class RegisterApi(APIView):
    def post(self, request):
        serializers_cls = RegisterSerializer(data=request.data)
        if serializers_cls.is_valid():
            user = serializers_cls.save()
            token_obj , _ =Token.objects.get_or_create(user=user)
            return Response({'user_id':user.id,'jwt_token':str(token_obj),'password':user.password},status=status.HTTP_200_OK)
        return Response('Invalid',status=status.HTTP_400_BAD_REQUEST)
    
class LoginToken(ObtainAuthToken):
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                         context={'request': request})
        if serializer.is_valid():
            user = serializer.validated_data['user']
            print(user,user.id)
            token, created = Token.objects.get_or_create(user=user)
            return Response({
                'token': token.key,
                'user_id': user.pk,
                'usre_name':user.username,
            },status=status.HTTP_200_OK)
        return Response('Invalid Login credtinala',status=status.HTTP_400_BAD_REQUEST)

class DetailsUsers(viewsets.ViewSet):
    def list(self,request):
        adv = User.objects.all()
        serializer = UserModelSerializer(adv,many=True)
        return Response(serializer.data)
    def retrieve(self,request,pk):
        id=pk
        if id is not None:
            adv = User.objects.get(id=id)
            serializer = UserModelSerializer(adv)
            return Response(serializer.data)
