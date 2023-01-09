from django.shortcuts import render
from .models import Event
from addresses.models import Address
from ongs.models import Ong
from .serializers import AddressSerializer, EventSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView, Response, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .permissions import IsAuthenticatedOrListOnly, IsOwnOngOrRetrieveOnly
from django.core.exceptions import ObjectDoesNotExist, ValidationError
from .errors import ValidationDateError


class EventView(ListCreateAPIView):

    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticatedOrListOnly]

    queryset = Event.objects.all()
    serializer_class = EventSerializer

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


class EventDetailView(RetrieveUpdateDestroyAPIView):

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
