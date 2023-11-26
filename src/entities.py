from src.builder import Builder


class Entities:
    def __init__(self, prefix: str, group_by: set):
        self.attributes = []
        self.prefix = prefix
        self.group_by = group_by
        self.builder = None

    def get_prefix(self):
        return self.prefix.lower()

    def get_attributes(self):
        attributes = {}

        for attribute in self.attributes:
            attributes[attribute] = f'{self.get_prefix()}_{attribute}'

        return attributes

    def get_objects(self) -> dict:
        return {}

    def query(self):
        self.builder = Builder(self).query()
        return self.builder
