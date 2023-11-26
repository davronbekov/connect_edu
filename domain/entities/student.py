from src.entities import Entities
from domain.entities.skill import Skills
from domain.entities.language import Languages


class Student(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Student", group_by=group_by)
        self.attributes = [
            'first_name',
            'second_name',
            'data_of_birth'
        ]

    def get_objects(self) -> dict:
        return {
            'has_skills': Skills(group_by={'skill_name'}),
            'can_speak': Languages(group_by={'language_name'})
        }
