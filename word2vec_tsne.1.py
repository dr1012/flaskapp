import pandas as pd
pd.options.mode.chained_assignment = None 
import numpy as np
import re
import nltk

from gensim.models import word2vec

from sklearn.manifold import TSNE
import matplotlib.pyplot as plt

import matplotlib as mpl
from wordcloud import WordCloud, STOPWORDS
from stopwords import stop_word_list
from pdf_extractor import extract

import spacy

stop_words =  stop_word_list()


text, tokens, keywords = extract('uploads/mytest.pdf')


for word in tokens:
    if word in stop_words:
        tokens.remove(word)  

cleantext = " ".join(tokens)



nlp = spacy.load('en_core_web_sm')  # make sure to use larger model!

doc = nlp(cleantext)
list_of_lists = []
for sentence in doc.sents:
    inner_list = []
    for token in sentence:
        inner_list.append(token.text)
    list_of_lists.append(inner_list) 
        




model = word2vec.Word2Vec(list_of_lists, size=50, window=10, min_count=1, workers=4)




def tsne_plot(model):
    "Creates and TSNE model and plots it"
    labels = []
    tokens = []

    #model.wv('trump') accesses the word vector for the word 'trump.

    #vocab is the list of words
    for word in model.wv.vocab:

        #model[word] is the matrix (word vector) of the word
        #same as model.wv but for the words in the vocab rather than just random words
        tokens.append(model[word])
       
        # word = word in the vocab, like 'sex', or 'work'...
        labels.append(word)
    
    tsne_model = TSNE(perplexity=40, n_components=2, init='pca', n_iter=1000, random_state=23)
    new_values = tsne_model.fit_transform(tokens)

    x = []
    y = []
    for value in new_values:
        x.append(value[0])
        y.append(value[1])
        
    plt.figure(figsize=(16, 16)) 
    for i in range(len(x)):
        plt.scatter(x[i],y[i])
        plt.annotate(labels[i],
                     xy=(x[i], y[i]),
                     xytext=(5, 2),
                     textcoords='offset points',
                     ha='right',
                     va='bottom')
    plt.show()


tsne_plot(model)



