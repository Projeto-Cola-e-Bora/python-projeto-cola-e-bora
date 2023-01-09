from .models import Event
from ongs.models import Ong
from ongs.serializers import OngSerializer
from .serializers import EventSerializer, AllEventsSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView,
    RetrieveAPIView,
    DestroyAPIView,
    ListAPIView,
)
from .permissions import IsAuthenticatedOrListOnly, IsNotOngOwnerOrRetrieveOnly
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .errors import ValidationDateError


class EventView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        try:
            ong = Ong.objects.get(id=request.data["ong_id"])
            serializer.save(ong=ong)
            return Response(serializer.data, status=201)
        except ObjectDoesNotExist:
            return Response(
                {"message": "Ong not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationDateError:
            return Response(
                {"message": "The event date cannot be a past date"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError:
            return Response(
                {"message": "Id must have a valid UUID format"},
                status=status.HTTP_404_NOT_FOUND,
            )


class EventDetailView(APIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    def patch(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            serializer = EventSerializer(event, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            serializer.save()
        except ObjectDoesNotExist:
            return Response(
                {"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationDateError:
            return Response(
                {"message": "The event date cannot be a past date"},
                status=status.HTTP_404_NOT_FOUND,
            )
        except ValidationError:
            return Response(
                {"message": "Id must have a valid UUID format"},
                status=status.HTTP_404_NOT_FOUND,
            )

        return Response(serializer.data)

    def delete(self, request, event_id):
        try:
            event = Event.objects.get(id=event_id)
            event.delete()
        except ObjectDoesNotExist:
            return Response(
                {"message": "Event not found"}, status=status.HTTP_404_NOT_FOUND
            )
        except ValidationError:
            return Response(
                {"message": "Id must have a valid UUID format"},
                status=status.HTTP_404_NOT_FOUND,
            )
        return Response(status=status.HTTP_204_NO_CONTENT)


class EventVolunteerView(CreateAPIView, DestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly, IsNotOngOwnerOrRetrieveOnly]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

    def get(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        serializer = self.get_serializer(event)

        return Response(serializer.data)

    def post(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        self.check_object_permissions(request, event)
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
