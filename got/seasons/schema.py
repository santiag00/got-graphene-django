from graphene import AbstractType, Node, Int, Float
from graphene_django.types import DjangoObjectType
from got.seasons.models import Season


class SeasonObject(DjangoObjectType):
    class Meta:
        model = Season
        interfaces = (Node,)

    number = Int(description="The number of the season")
    rating = Float(description="Rating of the season in the US (millions)")
