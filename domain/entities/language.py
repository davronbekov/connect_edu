from domain.entities.base import Base


class Languages(Base):
    def __init__(self, group_by: set):
        super().__init__(prefix="Languages", group_by=group_by)
        self.attributes = [
            'language_name'
        ]


