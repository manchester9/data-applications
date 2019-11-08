from nltk.book import *
import nltk 

print('\n')
print('printing corpus location')
print(nltk.__file__)
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