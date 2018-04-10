from graphene import AbstractType, Node, List, Field, String, Boolean
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from got.characters.models import Character
from got.loaders import get_data_loader
from got.places.loaders import PlaceLoader
from got.places.schema import PlaceObject
from got.seasons.models import Season
from got.seasons.schema import SeasonObject


class CharacterObject(DjangoObjectType):
    class Meta:
        model = Character
        interfaces = (Node,)
        filter_fields = ['first_name']

    first_name = String(description="The first name of the character")
    last_name = String(description="The last name of the character")
    is_alive = Boolean(description="The last name of the character")
    origin = Field(PlaceObject, description="The place where the character was born")
    seasons = List(SeasonObject, description="The seasons in which the character appears")

    def resolve_origin(self, info):
        return get_data_loader(PlaceLoader, info.context).load(self.origin_id)

    def resolve_seasons(self, info):
        return Season.objects.filter(character__id=self.id)


class Query(AbstractType):
    character = Node.Field(CharacterObject)
    characters = DjangoFilterConnectionField(CharacterObject)
