from domain.Education.entities.student import Student
from SPARQLWrapper import SPARQLWrapper2
from src.config import read_yaml

import nltk
from nltk.stem import WordNetLemmatizer
import re
from string import punctuation


nltk.download('punkt')
nltk.download('wordnet')


def normalize(text):
    processed_text = re.sub(f"[{re.escape(punctuation)}]", "", text)
    processed_text = " ".join(processed_text.split())
    return processed_text


def lemmatize(processed_text):
    wordnet_lemmatizer = WordNetLemmatizer()
    tokens = nltk.word_tokenize(processed_text)
    required_words = [wordnet_lemmatizer.lemmatize(x, 'v') for x in tokens]
    sentence_with_lemmnatized_word = " ".join(required_words)
    return sentence_with_lemmnatized_word


def process_text(text):
    text = normalize(text)
    text = lemmatize(text)
    return text


def create_pos_tags(sent):
    sent = nltk.word_tokenize(sent)
    sent = nltk.pos_tag(sent)
    return sent


items = [
    # 'Who studies Artificial Intelligence?',
    # 'Who lives in Coleridge Road?',
    'Who likes running?',
    # 'Who skilled in programming?',
    # 'Who graduates in 2024?',
    # 'Who speaks Russian?',
]

for item in items:
    print(create_pos_tags(process_text(item)))
    # attributes_list = ['study', 'live', 'like', 'skill', 'graduate', 'speak']

# q = Student(set()).query().get()
#
# config = read_yaml('config.yaml')
# sparql = SPARQLWrapper2(config['api_endpoint'])
# sparql.setQuery(q)
# result = sparql.query().bindings
#
# for x in result:
#     print(x)
