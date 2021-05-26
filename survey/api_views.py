from rest_framework.generics import ListAPIView, CreateAPIView, RetrieveUpdateDestroyAPIView, GenericAPIView

#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.filters import SearchFilter
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.response import Response

from survey.serializers import CitySerializer
from survey.models import City, State


class CityPagination(LimitOffsetPagination):
    default_limit = 10
    max_limit = 100


class CityList(ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer
#    filter_backends = (DjangoFilterBackend, SearchFilter)
#    filter_fields = ('id',)
#    search_fields = ('name' )
    pagination_class = CityPagination



class CityRetrieveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = City.objects.all()
    lookup_field = 'id'
    serializer_class = CitySerializer
