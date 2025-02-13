from django.utils import timezone
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from core.models import Favoritos, Livro
from core.serializers.favoritos import FavoritosSerializer, FavoritosCreateUpdateSerializer

class FavoritosViewSet(ModelViewSet):
    queryset = Favoritos.objects.all()
    serializer_class = FavoritosSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        usuario = self.request.user
        return Favoritos.objects.filter(usuario=usuario)

    def get_serializer_class(self):
        if self.action in ("create", "update"):
            return FavoritosCreateUpdateSerializer
        return FavoritosSerializer

    @action(detail=False, methods=["get"])
    def listar_favoritos(self, request):
        favoritos = self.get_queryset()
        serializer = self.get_serializer(favoritos, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)