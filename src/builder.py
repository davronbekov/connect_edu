from src.entities import Entities
from src.config import read_yaml


class Builder:
    def __init__(self):
        self.attributes = []
        self.groups = []
        self.queries = []

        conf = read_yaml('config.yaml')
        self.DOMAIN = conf['domain']

    def parse(self, cls: Entities, attrs: dict):
        for attribute in attrs:
            if attribute in cls.group_by:
                self.groups.append(
                    f'(GROUP_CONCAT(?{attrs[attribute]}; SEPARATOR=", ") AS ?{attrs[attribute]}s)'
                )
            else:
                self.attributes.append(f'?{attrs[attribute]}')

            self.queries.append(f'?{cls.get_prefix()} {self.DOMAIN}:{attribute} ?{attrs[attribute]}')

    def query(self, cls: Entities):
        self.queries = [f'?{cls.get_prefix()} a {self.DOMAIN}:{cls.prefix}']
        self.parse(cls, cls.get_attributes())

        relations = cls.get_objects()
        for relation in relations:
            relation_cls = relations[relation]

            self.queries.append(f'?{cls.get_prefix()} {self.DOMAIN}:{relation} ?{relation_cls.get_prefix()}')
            self.parse(relation_cls, relation_cls.get_attributes())

        print(self.attributes)
        print(self.groups)
        print(self.queries)

