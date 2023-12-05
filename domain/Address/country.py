from src.entities import Entities


class Country(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix='Countries', group_by=group_by)
        self.attributes = [
            'country_name'
        ]

