from nltk.book import *
import nltk
import re, nltk, pprint  

print('\n')
print('printing corpus location')
print(nltk.__file__)
import re, nltk, pprint
# from  __future__ import division

# generating text3 data
print('\n')
text3.generate()
text3.count('smote')

# generating text1 data
print('\n')
text1.concordance('monstrous')
print('processing frequency distribution')
print(FreqDist(text1))

print('\n')
print('long words')
V = set(text1)
long_words = [w for w in V if len(w) > 15]

print('\n')
sorted(long_words)
print(long_words)

# preprocessing data
print('\n')
print('bigrams processing')
print(bigrams(['more', 'is', 'said', 'than', 'done']))

print('\n')
print('gutenberg corpus')
print(nltk.corpus.gutenberg.fileids())

# loading your own corpus
from nltk.corpus import PlaintextCorpusReader
# corpus_root = '/usr/share/dict'

# accessing text from url
import urllib.request
url = "http://www.google.com"
request = urllib.request.Request(url)
response = urllib.request.urlopen(request)
print(response.read())

########################
# NLP pipeline
########################
# noise removal
noise_list = ["is", "a", "this", "..."] 
def _remove_noise(input_text):
    words = input_text.split() 
    noise_free_words = [word for word in words if word not in noise_list] 
    noise_free_text = " ".join(noise_free_words) 
    return noise_free_text

_remove_noise("this is a sample text")

# code to remove a regex pattern 
import re 
def _remove_regex(input_text, regex_pattern):
    urls = re.finditer(regex_pattern, input_text) 
    for i in urls: 
        input_text = re.sub(i.group().strip(), '', input_text)
    return input_text

regex_pattern = "#[\w]*"  

_remove_regex("remove this #hashtag from analytics vidhya", regex_pattern)


# stem and lemmatization
from nltk.stem.wordnet import WordNetLemmatizer 
lem = WordNetLemmatizer()

from nltk.stem.porter import PorterStemmer 
stem = PorterStemmer()

word = "multiplying" 
lem.lemmatize(word, "v")

stem.stem(word)


# object standardization 
lookup_dict = {'rt':'Retweet', 'dm':'direct message', "awsm" : "awesome", "luv" :"love"}
def _lookup_words(input_text):
    words = input_text.split() 
    new_words = [] 
    for word in words:
        if word.lower() in lookup_dict:
            word = lookup_dict[word.lower()]
        new_words.append(word) 
        new_text = " ".join(new_words) 
        return new_text

_lookup_words("RT this is a retweeted tweet by Shivam Bansal")
# >> "Retweet this is a retweeted tweet by Shivam Bansal"

# text to feature parsing 
from nltk import word_tokenize, pos_tag
text = "I am learning Natural Language Processing on Analytics Vidhya"
tokens = word_tokenize(text)
print(pos_tag(tokens))

# topic modeling
doc1 = "Sugar is bad to consume. My sister likes to have sugar, but not my father." 
doc2 = "My father spends a lot of time driving my sister around to dance practice."
doc3 = "Doctors suggest that driving may cause increased stress and blood pressure."
doc_complete = [doc1, doc2, doc3]
doc_clean = [doc.split() for doc in doc_complete]

import gensim
import corpora

# Creating the term dictionary of our corpus, where every unique term is assigned an index.  
dictionary = corpora.Dictionary(doc_clean)

# Converting list of documents (corpus) into Document Term Matrix using dictionary prepared above. 
doc_term_matrix = [dictionary.doc2bow(doc) for doc in doc_clean]

# Creating the object for LDA model using gensim library
Lda = gensim.models.ldamodel.LdaModel

# Running and Training LDA model on the document term matrix
ldamodel = Lda(doc_term_matrix, num_topics=3, id2word = dictionary, passes=50)

# Results 
print(ldamodel.print_topics())

def generate_ngrams(text, n):
    words = text.split()
    output = []  
    for i in range(len(words)-n+1):
        output.append(words[i:i+n])
    return output

generate_ngrams('this is a sample text', 2)

generate_ngrams('Need to input performance framework into the main section')
generate_ngrams('Need to put in text for conversational AI')
generate_ngrams('Need to get into the healthcare space for AI')


def parsing_content():
    pass 

def parsing_strings():
    pass 

def bigrams():
    pass 

def tokenization():
    pass 














































































