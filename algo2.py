#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  3 18:43:28 2018

@author: quentinvilchez
"""
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def virtual_documents(tweets, hashtags):
    '''
    @type tweets: list
    @type hashtags: list
    @type virtual (output):dictionnary
    Assumption: All hashtags found in @tweets are in the set @hashtags.
    Given a set of tweets and hashtags create a virtual document
    '''
    virtual = dict()

    for h in hashtags:
        virtual[h] =[]
    for t in tweets:
        if '#' in t:
            for h in hashtags:
                if h in t: 
                    virtual[h].append(t)
                else:
                    pass
        else:
            pass 
    return virtual

tokenize = lambda doc: doc.lower().split(" ")
stopwords =list(set(["a", "about", "above", "above", "across", "after", "afterwards", "again", "against", "all", "almost", "alone", "along", "already", "also","although","always","am","among", "amongst", "amoungst", "amount",  "an", "and", "another", "any","anyhow","anyone","anything","anyway", "anywhere", "are", "around", "as",  "at", "back","be","became", "because","become","becomes", "becoming", "been", "before", "beforehand", "behind", "being", "below", "beside", "besides", "between", "beyond", "bill", "both", "bottom","but", "by", "call", "can", "cannot", "cant", "co", "con", "could", "couldnt", "cry", "de", "describe", "detail", "do", "done", "down", "due", "during", "each", "eg", "eight", "either", "eleven","else", "elsewhere", "empty", "enough", "etc", "even", "ever", "every", "everyone", "everything", "everywhere", "except", "few", "fifteen", "fify", "fill", "find", "fire", "first", "five", "for", "former", "formerly", "forty", "found", "four", "from", "front", "full", "further", "get", "give", "go", "had", "has", "hasnt", "have", "he", "hence", "her", "here", "hereafter", "hereby", "herein", "hereupon", "hers", "herself", "him", "himself", "his", "how", "however", "hundred", "ie", "if", "in", "inc", "indeed", "interest", "into", "is", "it", "its", "itself", "keep", "last", "latter", "latterly", "least", "less", "ltd", "made", "many", "may", "me", "meanwhile", "might", "mill", "mine", "more", "moreover", "most", "mostly", "move", "much", "must", "my", "myself", "name", "namely", "neither", "never", "nevertheless", "next", "nine", "no", "nobody", "none", "noone", "nor", "not", "nothing", "now", "nowhere", "of", "off", "often", "on", "once", "one", "only", "onto", "or", "other", "others", "otherwise", "our", "ours", "ourselves", "out", "over", "own","part", "per", "perhaps", "please", "put", "rather", "re", "same", "see", "seem", "seemed", "seeming", "seems", "serious", "several", "she", "should", "show", "side", "since", "sincere", "six", "sixty", "so", "some", "somehow", "someone", "something", "sometime", "sometimes", "somewhere", "still", "such", "system", "take", "ten", "than", "that", "the", "their", "them", "themselves", "then", "thence", "there", "thereafter", "thereby", "therefore", "therein", "thereupon", "these", "they", "thickv", "thin", "third", "this", "those", "though", "three", "through", "throughout", "thru", "thus", "to", "together", "too", "top", "toward", "towards", "twelve", "twenty", "two", "un", "under", "until", "up", "upon", "us", "very", "via", "was", "we", "well", "were", "what", "whatever", "when", "whence", "whenever", "where", "whereafter", "whereas", "whereby", "wherein", "whereupon", "wherever", "whether", "which", "while", "whither", "who", "whoever", "whole", "whom", "whose", "why", "will", "with", "within", "without", "would", "yet", "you", "your", "yours", "yourself", "yourselves", "the"]))

def tfidf(virtual):
    """
    @type virtual: dictionnary
    @type output: tuple(scipy.sparse.csr.csr_matrix, list)
    Each virtual document is now represented as a feature
    vector based on the words in it using TF-IDF.
    """
    all_documents = []
    hashtag_in_order = []
    for i in virtual:
        hashtag_in_order.append(i)
        all_documents.append(' '.join(virtual[i]))
    sklearn_tfidf = TfidfVectorizer(norm='l2', stop_words= stopwords,min_df=0, use_idf=True, smooth_idf=False, sublinear_tf=True, tokenizer=tokenize)
    return (sklearn_tfidf.fit_transform(all_documents),hashtag_in_order)

    """
    Row 1 --> hashtag 1
    Row 2 --> hashtag 2
    ...
    
    Then simply use the cosine_similarity function that was imported and get the closest hashtags
    Only output first 100??

    
    """


    



