from src.entities import Entities


class Club(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Clubs", group_by=group_by)
        self.attributes = [
            'club_name',
        ]

