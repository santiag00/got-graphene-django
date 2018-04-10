from graphene import AbstractType, Node, String
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType

from got.places.models import Place


class PlaceObject(DjangoObjectType):
    class Meta:
        model = Place
        interfaces = (Node,)
        filter_fields = ['first_name']

    name = String(description="The name of the place")
    region = String(description="The region of the place")


class Query(AbstractType):
    place = Node.Field(PlaceObject)
    places = DjangoFilterConnectionField(PlaceObject)
