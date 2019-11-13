from rest_framework import viewsets
from . import models, serializers


class AbilityViewSet(viewsets.ModelViewSet):
    queryset = models.Ability.objects.all().order_by('pk')
    serializer_class = serializers.AbilitySerializer


class PokemonTypeViewSet(viewsets.ModelViewSet):
    queryset = models.PokemonType.objects.all().order_by('pk')
    serializer_class = serializers.PokemonTypeSerializer


class EggGroupViewSet(viewsets.ModelViewSet):
    queryset = models.EggGroup.objects.all().order_by('pk')
    serializer_class = serializers.EggGroupSerializer


class GenerationViewSet(viewsets.ModelViewSet):
    queryset = models.Generation.objects.all().order_by('pk')
    serializer_class = serializers.GenerationSerializer


class RegionViewSet(viewsets.ModelViewSet):
    queryset = models.Region.objects.all().order_by('pk')
    serializer_class = serializers.RegionSerializer


class PokemonViewSet(viewsets.ModelViewSet):
    queryset = models.Pokemon.objects.all().order_by('pk')
    serializer_class = serializers.PokemonSerializer
