from pdf_extractor import extract
import nltk.data
import spacy


text, tokens, keywords = extract('uploads/mytest.pdf')


def cleanText(text):
    # get rid of newlines
    text = text.strip().replace("\n", " ").replace("\r", " ").replace("\t", " ")
    text = " ".join(text.split())
    
    # lowercase
    text = text.lower()

    return text


mycleantext = " ".join(tokens)




nlp = spacy.load('en_core_web_sm')  # make sure to use larger model!

doc = nlp(mycleantext)

count = 0
for token in doc:
    if count < 5:
        print(token.vector)
        print('\n')
        print('\n')
        count = count + 1



