from rest_framework import status
from rest_framework.authtoken.admin import User
from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, ListAPIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from watch.serializers import CategorySerializer, WatchSerializer, UserCreateSerializer
from watch.models import Catgeory, Watch
from rest_framework.filters import SearchFilter

class CategoryItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Catgeory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticated, )

class CategoryListCreateAPIView(ListAPIView):
    queryset = Catgeory.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [SearchFilter]
    search_fields = ['simple']

class WatchItemUpdateDeleteAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = (IsAuthenticated, )

class WatchListCreateAPIView(ListCreateAPIView):
    queryset = Watch.objects.all()
    serializer_class = WatchSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, )
    filter_backends = [SearchFilter]
    search_fields = ['title']

@api_view(['POST'])
def register_views(request):
    serializer = UserCreateSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    User.objects.create_user(**serializer.validated_data)
    return Response(status=status.HTTP_201_CREATED)