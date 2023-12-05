from src.entities import Entities


class Hobby(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Hobbies', group_by=group_by)
        self.attributes = [
            'hobby_name'
        ]
