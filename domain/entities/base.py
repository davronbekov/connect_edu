

class Base:
    def __init__(self, prefix: str, group_by: set):
        self.attributes = []
        self.prefix = prefix
        self.group_by = group_by

    def get_prefix(self):
        return self.prefix.lower()

    def get_attributes(self):
        attributes = {}

        for attribute in self.attributes:
            attributes[attribute] = f'{self.get_prefix()}_{attribute}'

        return attributes

    def get_objects(self) -> dict:
        return {}
