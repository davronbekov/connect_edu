from src.entities import Entities


class Languages(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Languages", group_by=group_by)
        self.attributes = [
            'language_name'
        ]


