from .models import Event, EventVolunteers
from ongs.models import Ong
from .serializers import EventSerializer, EventVolunteersSerializer, AllEventsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status, APIView
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    RetrieveAPIView,
    ListAPIView,
)
from .permissions import IsAuthenticatedOrListOnly, IsNotOngOwnerOrRetrieveOnly
from datetime import datetime, timedelta


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


class EventVolunteerView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly, IsNotOngOwnerOrRetrieveOnly]


    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = EventSerializer(event)

        return Response(serializer.data)

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        self.check_object_permissions(request, event)

        registrated_user_events = EventVolunteers.objects.filter(user=request.user)

        serialized_event = AllEventsSerializer(event)
        serialized_user_events = EventVolunteersSerializer(registrated_user_events, many=True)

        event_date = serialized_event.data['date']
        event_date_format = datetime.fromisoformat(event_date)

        if len(serialized_user_events.data) > 0:
            for i in serialized_user_events.data:
                if(event_date_format > (i['event_time'] + timedelta(minutes=-60)) 
                and event_date_format < (i['event_time'] + timedelta(minutes=+60))):
                    return Response(
                        {"message": "You are already registered for an event at the same time"},
                        status=status.HTTP_400_BAD_REQUEST
                    )
            
        event.volunteers.add(request.user)

        return Response(
            {"message": "User succefully registrated on event."},
            status=status.HTTP_201_CREATED,
        )

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        self.check_object_permissions(request, event)
        event.volunteers.remove(request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)


class AllEventsView(ListAPIView):

    queryset = Event.objects.all()
    serializer_class = AllEventsSerializer


class EventsOngView(RetrieveAPIView):

    queryset = Event.objects.all()
    serializer_class = AllEventsSerializer

    def get(self, request, ong_id):
        ong = get_object_or_404(Ong, id=ong_id)
        event = Event.objects.filter(ong=ong)

        serializer = AllEventsSerializer(event, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
