from src.entities import Entities


class Campuse(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Campuses", group_by=group_by)
        self.attributes = [
            'campus_name',
        ]

