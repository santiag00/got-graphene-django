from graphene import ObjectType, Field, Schema
from graphene_django.debug import DjangoDebug

import got.characters.mutations
import got.characters.schema
import got.places.schema


class Mutations(ObjectType):
    create_character = got.characters.mutations.CreateCharacter.Field()


class Query(got.characters.schema.Query, got.places.schema.Query, ObjectType):
    debug = Field(DjangoDebug, name='__debug')


schema = Schema(query=Query, mutation=Mutations)
