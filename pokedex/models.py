from django.db import models


class Ability(models.Model):
    name = models.CharField(max_length=20)


class PokemonType(models.Model):
    name = models.CharField(max_length=20)


class EggGroup(models.Model):
    name = models.CharField(max_length=20)


class Generation(models.Model):
    name = models.CharField(max_length=20)


class Region(models.Model):
    name = models.CharField(max_length=20)
    descriptor = models.CharField(max_length=10)


class Pokemon(models.Model):
    national_dex = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=20)
    japanese_name = models.CharField(max_length=20)
    japanese_transliteration = models.CharField(max_length=50)
    japanese_romanized = models.CharField(max_length=50)
    has_mega = models.BooleanField()
    category = models.CharField(max_length=20)
    regional_numbers = models.ManyToManyField(
        Region,
        through='PokemonDex',
        related_name='pokemons',
    )
    egg_groups = models.ManyToManyField(EggGroup)
    hatch_time = models.IntegerField()
    experience_yield = models.IntegerField()
    gender_code = models.DecimalField(
        decimal_places=4,
        max_digits=4,
    )
    catch_rate = models.IntegerField()
    introduced_generation = models.ForeignKey(
        Generation,
        on_delete=models.CASCADE,
    )
    base_friendship = models.IntegerField()
    url = models.URLField()


class PokemonDex(models.Model):
    region = models.ForeignKey(
        Region,
        on_delete=models.CASCADE,
    )
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='regional_dex',
    )
    regional_dex = models.IntegerField()


class MegaStonePicture(models.Model):
    name = models.CharField(max_length=20)
    image_relative_link = models.CharField(max_length=500)
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='mega_stones',
    )


class Form(models.Model):
    name = models.CharField(max_length=20)
    image_relative_link = models.CharField(max_length=500)
    sprite_relative_link = models.CharField(max_length=500)
    abilities = models.ManyToManyField(
        Ability,
        through='FormAbility',
        related_name='forms',
    )
    types = models.ManyToManyField(
        PokemonType,
        through='FormType',
        related_name='forms',
    )
    weight = models.DecimalField(
        decimal_places=2,
        max_digits=5,
    )
    height = models.DecimalField(
        decimal_places=2,
        max_digits=5,
    )
    pokemon = models.ForeignKey(
        Pokemon,
        on_delete=models.CASCADE,
        related_name='forms',
    )


class FormAbility(models.Model):
    ability = models.ForeignKey(
        Ability,
        on_delete=models.CASCADE,
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='form_ability',
    )
    slot = models.CharField(
        max_length=2,
        choices=(
            ('F', 'First'),
            ('S', 'Second'),
            ('H', 'Hidden'),
            ('M', 'Mega'),
        ),
    )


class FormType(models.Model):
    pokemon_type = models.ForeignKey(
        PokemonType,
        on_delete=models.CASCADE,
    )
    form = models.ForeignKey(
        Form,
        on_delete=models.CASCADE,
        related_name='form_types',
    )
    slot = models.CharField(
        max_length=2,
        choices=(
            ('P', 'Primary'),
            ('S', 'Secondary'),
        ),
    )
