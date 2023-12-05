from src.entities import Entities


class Activity(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Activities', group_by=group_by)
        self.attributes = [
            'activity_name',
        ]
