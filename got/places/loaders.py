import typing
from promise import Promise

from got.loaders import DataLoader
from got.places.models import Place


class PlaceLoader(DataLoader):

    def batch_load_fn(self, place_ids: typing.List[int]) -> Promise:
        return Promise.resolve(PlaceLoader.get_places(place_ids))

    @staticmethod
    def get_places(place_ids: typing.List[int]) -> typing.List[Place]:
        places = Place.objects.filter(id__in=place_ids).in_bulk()
        return [places.get(place_id) for place_id in place_ids]
