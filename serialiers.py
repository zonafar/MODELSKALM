
from rest_framework import serializers
from .models import(
    depenseMissions, CoutDepensesMission, RecetteAvecPesage
    )

# SERIALIZER Missions
class depenseMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = depenseMissions
        fields = '__all__'

class CoutDepensesMissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = CoutDepensesMission
        fields = '__all__'

class RecetteAvecPesageSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecetteAvecPesage
        fields = '__all__'

class MissionsSerializer(serializers.ModelSerializer):
    infosDepenses = CoutDepensesMissionSerializer()
    produitsTransport = RecetteAvecPesageSerializer()


# SERIALIZER Maintenance
from .models import PiecesEchanges, Mantenances, InfosPieces

class PiecesEchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PiecesEchanges
        fields = '__all__'

class MantenanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mantenances
        fields = '__all__'

class InfosPieceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InfosPieces
        fields = '__all__'