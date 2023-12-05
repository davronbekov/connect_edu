from src.entities import Entities
from domain.Address.street import Street


class Location(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Location', group_by=group_by)
        self.attributes = [
            'address',
        ]

    def get_objects(self) -> dict:
        return {
            'location_street': Street(set()),
        }
