from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from account.models import CustomUser, Followers
from account.permissions import OwnerOrReadOnly
from account.serializers import UserSerializer, UserRegisterSerializer


# Create your views here.


class UserDetail(generics.RetrieveUpdateAPIView):

    """Получение или полное/частичное изменение данных пользователя по его user_name """

    permission_classes = [OwnerOrReadOnly]
    serializer_class = UserSerializer
    lookup_field = 'user_name'
    queryset = CustomUser.objects.all()


class UserRegistration(generics.CreateAPIView):
    permission_classes = (AllowAny,)
    serializer_class = UserRegisterSerializer
