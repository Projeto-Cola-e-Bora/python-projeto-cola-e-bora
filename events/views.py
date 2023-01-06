from .models import Event
from ongs.models import Ong
from .serializers import EventSerializer
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.views import Response, status
from django.shortcuts import get_object_or_404
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, RetrieveAPIView, DestroyAPIView
from .permissions import IsAuthenticatedOrListOnly, IsNotOngOwnerOrRetrieveOnly


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
            status=status.HTTP_201_CREATED
        )

    def delete(self, request, event_id):
        event = get_object_or_404(Event, id=event_id)
        self.check_object_permissions(request, event)
        event.volunteers.remove(request.user)

        return Response(status=status.HTTP_204_NO_CONTENT)


