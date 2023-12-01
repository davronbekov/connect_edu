from src.entities import Entities


class Faculty(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Faculties", group_by=group_by)
        self.attributes = [
            'faculty_name',
        ]

