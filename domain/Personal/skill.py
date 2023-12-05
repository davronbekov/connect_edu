from src.entities import Entities


class Skills(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Skills", group_by=group_by)
        self.attributes = [
            'skill_name'
        ]
