import pandas as pd


#setting frequency counters to zero for all categories
healthinfopositive = 0
healthinfoneutral = 0
healthinfonegative = 0
newspositive = 0
newsneutral = 0
newsnegative = 0
journalpositive = 0
journalneutral = 0
journalnegative = 0
personalpositive = 0
personalneutral = 0
personalnegative = 0
miscpositive = 0
miscneutral = 0
miscnegative = 0


df_json = pd.read_json('all_data_relevant_to_graph.json')
# imports the relevant columns of the json file for the perspectivegraph of sentiment, namely category and stanfordsentiment
df_stan_sentiment = df_json[['category', 'Stanford_sentiment']]

# the category of text the content came from is checked and the frequency is added to whichever category it belongs to
for index, row in df_stan_sentiment.iterrows():
    if (row[0]) == 'healthinfo':
        neutralscore = row[1].get('Neutral')
        if neutralscore == None:
            pass
        else:
            healthinfoneutral += neutralscore
        negativescore = row[1].get('Negative')
        if negativescore == None:
            pass
        else:
            healthinfonegative += negativescore
        positivescore = row[1].get('Positive')
        if positivescore == None:
            pass
        else:
            healthinfopositive += positivescore
    elif (row[0]) == 'news':
        neutralscore = row[1].get('Neutral')
        if neutralscore == None:
            pass
        else:
            newsneutral += neutralscore
        negativescore = row[1].get('Negative')
        if negativescore == None:
            pass
        else:
            newsnegative += negativescore
        positivescore = row[1].get('Positive')
        if positivescore == None:
            pass
        else:
            newspositive += positivescore
    elif (row[0]) == 'journal':
        neutralscore = row[1].get('Neutral')
        if neutralscore == None:
            pass
        else:
            journalneutral += neutralscore
        negativescore = row[1].get('Negative')
        if negativescore == None:
            pass
        else:
            journalnegative += negativescore
        positivescore = row[1].get('Positive')
        if positivescore == None:
            pass
        else:
            journalpositive += positivescore
    elif (row[0]) == 'personal':
        neutralscore = row[1].get('Neutral')
        if neutralscore == None:
            pass
        else:
            personalneutral += neutralscore
        negativescore = row[1].get('Negative')
        if negativescore == None:
            pass
        else:
            personalnegative += negativescore
        positivescore = row[1].get('Positive')
        if positivescore == None:
            pass
        else:
            personalpositive += positivescore
    elif (row[0]) == 'misc':
        neutralscore = row[1].get('Neutral')
        if neutralscore == None:
            pass
        else:
            miscneutral += neutralscore
        negativescore = row[1].get('Negative')
        if negativescore == None:
            pass
        else:
            miscnegative += negativescore
        positivescore = row[1].get('Positive')
        if positivescore == None:
            pass
        else:
            miscpositive += positivescore

#the dataframe that serves as a preliminary perspective graph in table format is initialized

ini_data = {
    'Text Category' : ['healthinfo', 'news', 'journal', 'personal', 'misc'],
    'Sentiment Frequency': [{'positive' : healthinfopositive,
                             'neutral' : healthinfoneutral,
                             'negative' : healthinfonegative},
                            {'positive': newspositive,
                             'neutral': newsneutral,
                             'negative': newsnegative},
                            {'positive' : journalpositive,
                             'neutral' : journalneutral,
                             'negative' : journalnegative},
                            {'positive' : personalpositive,
                             'neutral' : personalneutral,
                             'negative' : personalnegative},
                            {'positive' : miscpositive,
                             'neutral' : miscneutral,
                             'negative' : miscnegative}
                            ]
}
# the graph is exported to a tsv file.
#change the name accordingly.
perspective_graph = pd.DataFrame(ini_data)
perspective_graph.to_csv('perspective_graphstan.tsv', index = False, sep = '\t', encoding = 'utf-8')