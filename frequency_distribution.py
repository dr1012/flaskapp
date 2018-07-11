import nltk
from nltk import FreqDist
import pygal

def  frequency_dist(data, n, title ):

    #data should be a list of words
    #n is number of most common words


    dist = FreqDist(data)

    most_common=dist.most_common(n)

    words_ordered = []
    frequencies_ordered = []
    for word in most_common:
        words_ordered.append(word[0])
        frequencies_ordered.append(word[1])




    line_chart = pygal.Bar()
    line_chart.title = 'Word frequency'
    line_chart.x_labels = words_ordered

    line_chart = pygal.HorizontalBar()
    line_chart.title = title

    for i in range(len(words_ordered)):
        line_chart.add(words_ordered[i], frequencies_ordered[i])
    return line_chart.render_data_uri()

