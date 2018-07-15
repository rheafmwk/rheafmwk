import spacy
from spacy.tokens.doc import Doc
from nltk import tokenize
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import rake
from py2neo import Graph, authenticate
import operator
import io
import os
import sys
import json
import re

authenticate("hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24789", "rheauser", "b.tvYI5zZ7SWCQ.l04N5jzsNkbFCzFf")
g = Graph("http://hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24789", bolt = False)

#authenticate("hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24780", "rheauser", "b.tvYI5zZ7SWCQ.l04N5jzsNkbFCzFf")
#g = Graph("bolt://hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24786", user="rheauser", password="b.tvYI5zZ7SWCQ.l04N5jzsNkbFCzFf", bolt=True, secure = True, http_port = 24789, https_port = 24780)
#g = Graph("https://hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24789", bolt = False)

fileDir = os.path.dirname(os.path.realpath('__file__'))
stoppath = os.path.join(fileDir, "src/static/assets/SmartStoplist.txt")
rake_object = rake.Rake(stoppath, 5, 3, 2)
nlp = spacy.load('en')
loc = os.path.join(fileDir, "src/static/assets/flowsSerialized")
docs = []
namedict = g.run('MATCH (n:Flow) RETURN n.title, n.doc_id, n.description, n.referenceURL').data()

for file in os.listdir(loc):
    if file.endswith(".bin"):
        #print(file)
        filename = re.sub('\.bin$', '', file)
        myid = ""
        mydesc = ""
        myref = ""
        for item in namedict:
            if item["n.doc_id"] == filename:
                myid = item["n.title"]
                mydesc = item["n.description"]
                myref = item["n.referenceURL"]
        for byte_string in Doc.read_bytes(open(os.path.join(loc,file), 'rb')):
           doc = Doc(nlp.vocab)
           doc.from_bytes(byte_string)
           #print(myid)
           doc.user_data['id']=myid
           doc.user_data['desc']=mydesc
           doc.user_data['ref']=myref
           docs.append(doc)


def getanalysis(flow):

    text = flow['description']
    keywlist = []
    keywords = rake_object.run(text)
    for item in keywords:
        keywlist.append([item[0],item[1]])
    #print("keywords:")
    #print(keywords)
    #print("sentiment:")
    lines_list = tokenize.sent_tokenize(text)
    sid = SentimentIntensityAnalyzer()
    i = 0
    score = 0.0
    for sentence in lines_list:
        sisc = sid.polarity_scores(sentence)
        score = score + sisc['compound']
        i = i + 1
    finalscore = score/i
    #print(finalscore)
    ranking = {}
    mydoc = nlp(text)
    for doc in docs:
        myid = doc.user_data['id']
        mydesc = doc.user_data['desc']
        myref = doc.user_data['ref']
        if(myid):
            score = mydoc.similarity(doc)
            ranking.update({score: [myid, mydesc, myref]})
        #print(doc.text)
    sorted_x = sorted(ranking.items(), key=operator.itemgetter(0), reverse=True)
    print(sorted_x)
    rdict = {"sentiment":finalscore, "keywords":keywlist, "flowranking":sorted_x}
    return (json.dumps(rdict))
    
    