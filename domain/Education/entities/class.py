from src.entities import Entities


class Class(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Classes", group_by=group_by)
        self.attributes = [
            'start_year',
            'graduate_year',
        ]

