from src.entities import Entities


class Course(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Courses", group_by=group_by)
        self.attributes = [
            'course_code',
            'course_name',
        ]

