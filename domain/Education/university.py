from src.entities import Entities
from domain.Education.campus import Campus


class University(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Universities", group_by=group_by)
        self.attributes = [
            'university_name',
        ]

    def get_objects(self) -> dict:
        return {
            'uni_campuses': Campus(set())
        }

