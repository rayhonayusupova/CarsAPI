from rest_framework.generics import CreateAPIView
from .serializers import SingUpSerializer,CarSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet,ModelViewSet
from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Car
from .permissions import IsOwner

class SignUpView(CreateAPIView):
    serializer_class=SingUpSerializer


@extend_schema(
    tags=['Public cars']
    )
class PublicCarViewSet(ReadOnlyModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer 
    permission_classes=[AllowAny]

@extend_schema(
    tags=['My cars']
    )
class UserCarViewSet(ModelViewSet):
    serializer_class = CarSerializer
    permission_classes = [IsAuthenticated, IsOwner]

    def get_queryset(self):
        return Car.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)
