import csv
import nltk
import re
import urllib
from nltk.corpus import wordnet
import numpy as np

with open('hashtags.csv', 'r') as f:
    reader = csv.reader(f)
    csv_file = list(reader)

hashtag_list = list()

for i in csv_file:
    hashtag_list.append(i[1])

hashtag_list = hashtag_list[100:105]
hashtag_dict = dict()


def lookup(hashtag):
    english_vocab = set(w.lower() for w in nltk.corpus.words.words())
    return (hashtag.lower() in english_vocab)


def synset_finder(hashtag):
    pos = ['r', 's', 'a', 'v', 'n']
    synset = None
    for i in pos:
        try:
            synset = wordnet.synset(hashtag + '.' + i + '.01')
        except nltk.corpus.reader.wordnet.WordNetError:
            pass
    return synset

def metaData_algorithm(hashtag_list):
    rgx_two = re.compile('\w*[A-Z]\w*[A-Z]\w*')
    rgx_one = re.compile('\w*[A-Z]\w*')
    for hashtag in hashtag_list:
        hashtag_dict[hashtag] = []

    for hashtag in hashtag_dict.keys():
        print hashtag
        if not rgx_one.match(hashtag) and not lookup(hashtag):
            hashtag_alias = hashtag[:]

            while not lookup(hashtag_alias) and len(hashtag_alias) != 0:
                hashtag_alias = hashtag_alias[:-1]
            if lookup(hashtag_alias):
                hashtag_dict[hashtag_alias] = synset_finder(hashtag_alias)
            else:
                print(hashtag_alias)
                print("Wiki look")  # urllib.urlopen("https://en.wikipedia.org/wiki/" + hashtag_alias).getcode()
        else:
            if lookup(hashtag):
                hashtag_dict[hashtag] = synset_finder(hashtag)
            elif rgx_two.match(hashtag):
                subtag = re.findall('[A-Z][^A-Z]*', hashtag)[0]  # Check with data whether to drop [-1] or [0]
                if lookup(subtag):
                    hashtag_dict[hashtag] = synset_finder(subtag)
                else:
                    print(hashtag)
            else:
                print(hashtag)

    return hashtag_dict


syn_dict = metaData_algorithm(hashtag_list)
print(syn_dict)


def matrix_creation(syn_dict):
    ((k, v) for k, v in hashtag_dict.iteritems() if v)
    size = len(hashtag_dict)
    matrix = np.zeros((size, size))
    key_list = list(syn_dict.keys())
    print key_list
    for i in range(len(key_list)):
        for j in range(len(key_list)):
            if i > j:
                print(key_list[i], key_list[j])
                try:
                    d = wordnet.wup_similarity(syn_dict[key_list[i]], syn_dict[key_list[j]])
                    matrix[i][j] = float(d)
                except:
                    pass
            elif i == j:
                matrix[i][j] = 1
    return matrix

print(matrix_creation(syn_dict))
# def metaData(hashtag_list):
#     english_vocab = set(w.lower() for w in nltk.corpus.words.words())
#     LC_h = list()
#     if hashtag_list is not None:
#         for hashtag in hashtag_list:
#             rgx = re.compile('\w*[A-Z]\w*[A-Z]\w*')
#             if hashtag.lower() in english_vocab:
#                 LC_h.append(hashtag.lower())
#             elif rgx.match(hashtag):
#                 subtag_list = re.findall('[A-Z][^A-Z]*', hashtag)
#                 LC_h.append(metaData(subtag_list))
#             else:
#                 print urllib.urlopen("https://en.wikipedia.org/wiki/" + hashtag).getcode()
#         return [x for x in LC_h if x is not None]
#     else:
#         pass
