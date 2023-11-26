from domain.entities.base import Base
from domain.core import DOMAIN


class Builder:
    def __init__(self):
        self.attributes = []
        self.groups = []
        self.queries = []

    def parse(self, cls: Base, attrs: dict):
        for attribute in attrs:
            if attribute in cls.group_by:
                self.groups.append(
                    f'(GROUP_CONCAT(?{attrs[attribute]}; SEPARATOR=", ") AS ?{attrs[attribute]}s)'
                )
            else:
                self.attributes.append(f'?{attrs[attribute]}')

            self.queries.append(f'?{cls.get_prefix()} {DOMAIN}:{attribute} ?{attrs[attribute]}')

    def query(self, cls: Base):
        self.queries = [f'?{cls.get_prefix()} a {DOMAIN}:{cls.prefix}']
        self.parse(cls, cls.get_attributes())

        relations = cls.get_objects()
        for relation in relations:
            relation_cls = relations[relation]

            self.queries.append(f'?{cls.get_prefix()} {DOMAIN}:{relation} ?{relation_cls.get_prefix()}')
            self.parse(relation_cls, relation_cls.get_attributes())

        print(self.attributes)
        print(self.groups)
        print(self.queries)

