from src.entities import Entities


class Module(Entities):
    def __init__(self, group_by: set):
        super().__init__(prefix="Modules", group_by=group_by)
        self.attributes = [
            'module_code',
            'module_name',
        ]

