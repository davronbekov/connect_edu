from src.entities import Entities
from domain.Education.faculty import Faculty
from domain.Education.club import Club
from domain.Address.location import Location


class Campus(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Campuses", group_by=group_by)
        self.attributes = [
            'campus_name',
        ]

    def get_objects(self) -> dict:
        return {
            'cam_faculty': Faculty(set()),
            'cam_club': Club(set()),
            'cam_located': Location(set())
        }


