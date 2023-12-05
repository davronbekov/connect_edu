from src.entities import Entities
from domain.Education.course import Course


class Faculty(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Faculties", group_by=group_by)
        self.attributes = [
            'faculty_name',
        ]

    def get_objects(self) -> dict:
        return {
            'fac_course': Course(set())
        }

