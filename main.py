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
# sparql = SPARQLWrapper2("http://localhost:3030/connect_edu/query")
#
# query_start = """
#                 PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
#                 PREFIX con: <http://www.w3.org/2000/10/swap/pim/contact#>
#                 PREFIX co: <http://purl.org/ontology/co/core#>
#                 PREFIX rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#>
#                 PREFIX connect: <http://connect.edu/ontologies#>
#
#                 SELECT
#                 ?first_name
#                 ?second_name
#                 ?start_year
#                 ?graduate_year
#                 ?course_name
#                 (GROUP_CONCAT(?skill_name; SEPARATOR=", ") AS ?skill_names)
#                 (GROUP_CONCAT(?language_name; SEPARATOR=", ") AS ?language_names)
#                 ?address
#                 ?street_name
#                 ?postcode
#                 WHERE {
#                   ?student a connect:Students.
#                   ?student connect:first_name ?first_name.
#                   ?student connect:second_name ?second_name.
#                   ?student connect:student_class ?student_class.
#                   ?student_class connect:start_year ?start_year.
#                   ?student_class connect:graduate_year ?graduate_year.
#                   ?student_class connect:class_course ?class_course.
#                   ?class_course connect:course_name ?course_name.
#                   ?student connect:can_speak ?languages.
#                   ?languages connect:language_name ?language_name.
#                   ?student connect:has_skills ?skills.
#                   ?skills connect:skill_name ?skill_name.
#                   ?student connect:person_lives ?location.
#                   ?location connect:address ?address.
#                   ?location connect:location_street ?street.
#                   ?street connect:street_name ?street_name.
#                   ?street connect:street_of_postcode ?street_postcode.
#                   ?street_postcode connect:postcode ?postcode.
#                   FILTER (?course_name="Artificial intelligence").
#                   FILTER(?language_name="Russian").
#                   FILTER(?skill_name="Programming").
#                 }
#                 GROUP BY ?first_name ?second_name ?start_year ?graduate_year ?course_name ?address ?street_name ?postcode
#               """
# query_end = ""
#
# query = query_start + query_end
# sparql.setQuery(query)
# result = sparql.query().bindings
#
# for x in result:
#     print(x)


from domain.entities.student import Student
from domain.entities.skill import Skills
from SPARQLWrapper import SPARQLWrapper2
from src.config import read_yaml

q = ' '.join(Student(set()).query().get())
print(q)

config = read_yaml('config.yaml')

sparql = SPARQLWrapper2("http://localhost:3030/connect_edu/query")
sparql.setQuery(q)
result = sparql.query().bindings

for x in result:
    print(x)


