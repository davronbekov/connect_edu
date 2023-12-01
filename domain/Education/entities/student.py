from src.entities import Entities
from domain.Personal.entities.skill import Skills
from domain.Personal.entities.language import Languages


class Student(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Students", group_by=group_by)
        self.attributes = [
            'first_name',
            'second_name',
        ]

    def get_objects(self) -> dict:
        return {
            'has_skills': Skills(group_by={'skill_name'}),
            'can_speak': Languages(group_by={'language_name'})
        }
