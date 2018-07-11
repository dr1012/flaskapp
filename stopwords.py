from spacy.lang.en.stop_words import STOP_WORDS
import nltk

#STOP_WORDS.add("your_additional_stop_word_here")



def stop_word_list():
    
    nltk_stopwords = nltk.corpus.stopwords.words('english')

    for word in STOP_WORDS:
        if word not in nltk_stopwords:
            nltk_stopwords.append(word)

    return nltk_stopwords        



