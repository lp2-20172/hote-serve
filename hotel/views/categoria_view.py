from ..models.categoria import Categoria
from rest_framework import serializers, viewsets
from rest_framework import permissions


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    #permission_classes = [permissions.IsAuthenticated]
