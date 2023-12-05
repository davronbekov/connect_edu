from src.entities import Entities
from domain.Personal.skill import Skills
from domain.Personal.language import Languages
from domain.Personal.hobby import Hobby
from domain.Personal.activity import Activity
from domain.Address.location import Location
from domain.Education.classes import Class


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
            'can_speak': Languages(group_by={'language_name'}),
            'person_lives': Location(set()),
            'student_class': Class(set()),
            'liked_hobby': Hobby(set()),
            'preferred_activity': Activity(group_by={'activity_name'})
        }
