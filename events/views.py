from django.shortcuts import render
from .models import Event
from ongs.models import Ong
from addresses.models import Address
from ongs.models import Ong
from ongs.serializers import OngSerializer
from .serializers import AddressSerializer, EventSerializer, AllEventsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    ListAPIView,
    RetrieveAPIView,
)
from .permissions import IsAuthenticatedOrListOnly, IsOwnOngOrRetrieveOnly


class EventView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        ong = Ong.objects.get(id=request.data["ong_id"])
        serializer.save(ong=ong)
        return Response(serializer.data, status=201)


class EventDetailView(RetrieveUpdateDestroyAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    def patch(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = EventSerializer(event, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response(serializer.data)

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        event.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class ListAllEventsView(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = AllEventsSerializer


class ListEventsOngView(RetrieveAPIView):
    def retrieve(self, request, ong_id):
        ong = get_object_or_404(Ong, id=ong_id)
        serializer = OngSerializer(ong)
        return Response(serializer.data, status=status.HTTP_200_OK)
