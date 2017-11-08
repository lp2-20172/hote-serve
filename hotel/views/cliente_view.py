from ..models.cliente import Cliente
from rest_framework import serializers, viewsets
from rest_framework import permissions


class ClienteSerializer(serializers.ModelSerializer):
    person_nombre = serializers.SerializerMethodField()
    person_apellido = serializers.SerializerMethodField()

    class Meta:
        model = Cliente
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')

    def get_person_nombre(self, obj):
        return "%s " % (obj.person.first_name)

    def get_person_apellido(self, obj):
        return "%s " % (obj.person.last_name)


class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    #permission_classes = [permissions.IsAuthenticated]
