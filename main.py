from domain.Education.student import Student
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


#     'Who loves Running?',
#     'Who skilled in programming?',
#     'Who graduates in 2024?',
#     'Who enrolled in 2023?',
#     'Who speaks Russian?',

print('Please, write your text:')
text = input()
pos_tags = create_pos_tags(process_text(text))

bag_of_words = {
    'skilled': 'skills_skill_names',
    'graduate': 'classes_graduate_year',
    'enrol': 'classes_start_year',
    'love': 'activities_activity_name',
    'speak': 'languages_language_name',
}

students = Student(set()).query().where(bag_of_words[pos_tags[1][0]], pos_tags[-1][0]).get()

config = read_yaml('config.yaml')
sparql = SPARQLWrapper2(config['api_endpoint'])
sparql.setQuery(students)
result = sparql.query().bindings

for i, data in enumerate(result):
    print(f'Student #{i + 1}')
    for key in data:
        print(f'{key}: {data[key].value}')
