from src.entities import Entities
from domain.Address.country import Country


class City(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Cities', group_by=group_by)
        self.attributes = [
            'city_name',
        ]

    def get_objects(self) -> dict:
        return {
            'city_of': Country(set()),
        }
