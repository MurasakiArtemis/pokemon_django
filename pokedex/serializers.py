from rest_framework import serializers
from . import models


class AbilitySerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Ability
        fields = '__all__'


class PokemonTypeSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.PokemonType
        fields = '__all__'


class EggGroupSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.EggGroup
        fields = '__all__'


class GenerationSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Generation
        fields = '__all__'


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Region
        fields = '__all__'


class PokemonSerializer(serializers.ModelSerializer):

    class Meta:
        model = models.Pokemon
        fields = '__all__'