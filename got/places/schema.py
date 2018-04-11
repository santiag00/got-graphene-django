from graphene import AbstractType, Node, String
from graphene_django.types import DjangoObjectType
from graphene_django import DjangoConnectionField

from got.places.models import Place


class PlaceObject(DjangoObjectType):
    class Meta:
        model = Place
        interfaces = (Node,)

    name = String(description="The name of the place")
    region = String(description="The region of the place")

class Query(AbstractType):
    places = DjangoConnectionField(PlaceObject)
