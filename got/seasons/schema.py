from graphene import AbstractType, Node, Int, Float
from graphene_django.filter import DjangoFilterConnectionField
from graphene_django.types import DjangoObjectType
from got.seasons.models import Season


class SeasonObject(DjangoObjectType):
    class Meta:
        model = Season
        interfaces = (Node,)
        filter_fields = ['number']

    number = Int(description="The number of the season")
    rating = Float(description="Rating of the season in the US (millions)")


class Query(AbstractType):
    season = Node.Field(SeasonObject)
    seasons = DjangoFilterConnectionField(SeasonObject)
