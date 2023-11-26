# from SPARQLWrapper import SPARQLWrapper2
# import stanza
#
# stanza.download('en')
#
# nlp = stanza.Pipeline('en', processors='tokenize,lemma,pos,ner')
#
# items = [
#     # 'Who studies Artificial Intelligence?',
#     # 'Who lives in Coleridge Road?',
#     'Who likes running?',
#     # 'Who skilled in programming?',
#     # 'Who graduates in 2024?',
#     # 'Who speaks Russian?',
# ]
#
# for item in items:
#     doc = nlp(item)
#     attributes_list = ['study', 'live', 'like', 'skill', 'graduate', 'speak']
#
#     print(doc)
#     print(doc.entities)
# exit()

from domain.entities.student import Student
from SPARQLWrapper import SPARQLWrapper2
from src.config import read_yaml

q = Student(set()).query().where('students_first_name', 'Otabek').get()
print(q)

config = read_yaml('config.yaml')

sparql = SPARQLWrapper2(config['api_endpoint'])
sparql.setQuery(q)
result = sparql.query().bindings

for x in result:
    print(x)


