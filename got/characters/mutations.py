from graphene import ObjectType, InputObjectType, String, Field, Boolean, List, Int
from graphene.relay import ClientIDMutation

from got.characters.schema import CharacterObject
from got.characters.models import Character
from got.places.models import Place
from got.seasons.models import Season


class CreateCharacter(ClientIDMutation):
    class Input:
        first_name = String(required=True)
        last_name = String(required=True)
        is_alive = Boolean(required=True)
        origin_id = Int(required=True)
        seasons = List(Int)

    character = Field(lambda: CharacterObject)

    @classmethod
    def mutate_and_get_payload(cls, root, info, **input):
        origin = Place.objects.get(id=input['origin_id'])
        seasons = Season.objects.filter(number__in=input['seasons'])

        character = Character.objects.create(
            first_name=input['first_name'],
            last_name=input['last_name'],
            is_alive=input['is_alive'],
            origin=origin,
        )
        character.seasons.set(seasons)

        return CreateCharacter(character=character)
