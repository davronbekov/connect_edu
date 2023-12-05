from src.entities import Entities
from domain.Address.city import City


class Postcode(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Postcodes', group_by=group_by)
        self.attributes = [
            'postcode',
        ]

    def get_objects(self) -> dict:
        return {
            'postcode_of_city': City(set()),
        }
