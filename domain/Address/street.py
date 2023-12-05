from src.entities import Entities
from domain.Address.postcode import Postcode


class Street(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Streets', group_by=group_by)
        self.attributes = [
            'street_name',
        ]

    def get_objects(self) -> dict:
        return {
            'street_of_postcode': Postcode(set())
        }
