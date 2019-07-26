from py2neo import Graph
import json

graphURL = 'http://hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24789'
graphUser = 'rheauser'
graphPass = 'b.tvYI5zZ7SWCQ.l04N5jzsNkbFCzFf'

#graphURL = 'https://rheafmwk.io:7473'
#graphUser = 'rhea'
#graphPass = 'rheafmwk2019'

g = Graph(graphURL, user=graphUser, password=graphPass)




def getflowdata(d):
    
    #d => get page string from json
    t = d['title']
    rdict = []
    if(t == "PTI"):
        emodict = g.run('MATCH (y:CoreFlow)-[r]->(n:Flow)-[x:TOUCHESON]->(u:Emotion) WHERE y.cf_id="PTI" RETURN u.name, x.weight').data()
        joyArray = [d['x.weight'] for d in emodict if d["u.name"] == "Joy"]        
        anticipationArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anticipation"]
        sadnessArray = [d['x.weight'] for d in emodict if d["u.name"] == "Sadness"]
        disgustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Disgust"]
        angerArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anger"]
        fearArray = [d['x.weight'] for d in emodict if d["u.name"] == "Fear"]
        surpriseArray = [d['x.weight'] for d in emodict if d["u.name"] == "Surprise"]
        trustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Trust"]
        joy = reduce(lambda x, y: x + y, joyArray) / len(joyArray)
        anticipation = reduce(lambda x, y: x + y, anticipationArray) / len(anticipationArray)
        sadness = reduce(lambda x, y: x + y, sadnessArray) / len(sadnessArray)
        disgust = reduce(lambda x, y: x + y, disgustArray) / len(disgustArray)
        anger = reduce(lambda x, y: x + y, angerArray) / len(angerArray)
        fear = reduce(lambda x, y: x + y, fearArray) / len(fearArray)
        surprise = reduce(lambda x, y: x + y, surpriseArray) / len(surpriseArray)
        trust = reduce(lambda x, y: x + y, trustArray) / len(trustArray)
        emotions = [joy, anticipation, sadness, disgust, anger, fear, surprise, trust]
        normemotions = [int(round((float(i)/max(emotions))*100)) for i in emotions]
        emotiondict = {'joy': normemotions[0], 'anticipation': normemotions[1], 'sadness': normemotions[2], 'disgust': normemotions[3], 'anger': normemotions[4], 'fear': normemotions[5], 'surprise': normemotions[6], 'trust': normemotions[7]}
                
        namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="PTI" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="PTI" RETURN b.name, count(b)').data()            
        rdict = {"relatedflows":namedict, "upphases": uppDict, "emotionlandscape":emotiondict}
        #"up":upcount, "keywords":keywlist, 
    
    if(t == "OFC"):
        emodict = g.run('MATCH (y:CoreFlow)-[r]->(n:Flow)-[x:TOUCHESON]->(u:Emotion) WHERE y.cf_id="OFC" RETURN u.name, x.weight').data()
        joyArray = [d['x.weight'] for d in emodict if d["u.name"] == "Joy"]        
        anticipationArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anticipation"]
        sadnessArray = [d['x.weight'] for d in emodict if d["u.name"] == "Sadness"]
        disgustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Disgust"]
        angerArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anger"]
        fearArray = [d['x.weight'] for d in emodict if d["u.name"] == "Fear"]
        surpriseArray = [d['x.weight'] for d in emodict if d["u.name"] == "Surprise"]
        trustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Trust"]
        joy = reduce(lambda x, y: x + y, joyArray) / len(joyArray)
        anticipation = reduce(lambda x, y: x + y, anticipationArray) / len(anticipationArray)
        sadness = reduce(lambda x, y: x + y, sadnessArray) / len(sadnessArray)
        disgust = reduce(lambda x, y: x + y, disgustArray) / len(disgustArray)
        anger = reduce(lambda x, y: x + y, angerArray) / len(angerArray)
        fear = reduce(lambda x, y: x + y, fearArray) / len(fearArray)
        surprise = reduce(lambda x, y: x + y, surpriseArray) / len(surpriseArray)
        trust = reduce(lambda x, y: x + y, trustArray) / len(trustArray)
        emotions = [joy, anticipation, sadness, disgust, anger, fear, surprise, trust]
        normemotions = [int(round((float(i)/max(emotions))*100)) for i in emotions]
        emotiondict = {'joy': normemotions[0], 'anticipation': normemotions[1], 'sadness': normemotions[2], 'disgust': normemotions[3], 'anger': normemotions[4], 'fear': normemotions[5], 'surprise': normemotions[6], 'trust': normemotions[7]}
        
        namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="OFC" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="OFC" RETURN b.name, count(b)').data()            
        rdict = {"relatedflows":namedict, "upphases": uppDict, "emotionlandscape":emotiondict}
    
    if(t == "FTC"):
            emodict = g.run('MATCH (y:CoreFlow)-[r]->(n:Flow)-[x:TOUCHESON]->(u:Emotion) WHERE y.cf_id="FTC" RETURN u.name, x.weight').data()
            joyArray = [d['x.weight'] for d in emodict if d["u.name"] == "Joy"]        
            anticipationArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anticipation"]
            sadnessArray = [d['x.weight'] for d in emodict if d["u.name"] == "Sadness"]
            disgustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Disgust"]
            angerArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anger"]
            fearArray = [d['x.weight'] for d in emodict if d["u.name"] == "Fear"]
            surpriseArray = [d['x.weight'] for d in emodict if d["u.name"] == "Surprise"]
            trustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Trust"]
            joy = reduce(lambda x, y: x + y, joyArray) / len(joyArray)
            anticipation = reduce(lambda x, y: x + y, anticipationArray) / len(anticipationArray)
            sadness = reduce(lambda x, y: x + y, sadnessArray) / len(sadnessArray)
            disgust = reduce(lambda x, y: x + y, disgustArray) / len(disgustArray)
            anger = reduce(lambda x, y: x + y, angerArray) / len(angerArray)
            fear = reduce(lambda x, y: x + y, fearArray) / len(fearArray)
            surprise = reduce(lambda x, y: x + y, surpriseArray) / len(surpriseArray)
            trust = reduce(lambda x, y: x + y, trustArray) / len(trustArray)
            emotions = [joy, anticipation, sadness, disgust, anger, fear, surprise, trust]
            normemotions = [int(round((float(i)/max(emotions))*100)) for i in emotions]
            emotiondict = {'joy': normemotions[0], 'anticipation': normemotions[1], 'sadness': normemotions[2], 'disgust': normemotions[3], 'anger': normemotions[4], 'fear': normemotions[5], 'surprise': normemotions[6], 'trust': normemotions[7]}
        
            namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="FTC" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
            uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="FTC" RETURN b.name, count(b)').data()            
            rdict = {"relatedflows":namedict, "upphases": uppDict, "emotionlandscape":emotiondict}
    
    if(t == "STE"):
            emodict = g.run('MATCH (y:CoreFlow)-[r]->(n:Flow)-[x:TOUCHESON]->(u:Emotion) WHERE y.cf_id="STE" RETURN u.name, x.weight').data()
            joyArray = [d['x.weight'] for d in emodict if d["u.name"] == "Joy"]        
            anticipationArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anticipation"]
            sadnessArray = [d['x.weight'] for d in emodict if d["u.name"] == "Sadness"]
            disgustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Disgust"]
            angerArray = [d['x.weight'] for d in emodict if d["u.name"] == "Anger"]
            fearArray = [d['x.weight'] for d in emodict if d["u.name"] == "Fear"]
            surpriseArray = [d['x.weight'] for d in emodict if d["u.name"] == "Surprise"]
            trustArray = [d['x.weight'] for d in emodict if d["u.name"] == "Trust"]
            joy = reduce(lambda x, y: x + y, joyArray) / len(joyArray)
            anticipation = reduce(lambda x, y: x + y, anticipationArray) / len(anticipationArray)
            sadness = reduce(lambda x, y: x + y, sadnessArray) / len(sadnessArray)
            disgust = reduce(lambda x, y: x + y, disgustArray) / len(disgustArray)
            anger = reduce(lambda x, y: x + y, angerArray) / len(angerArray)
            fear = reduce(lambda x, y: x + y, fearArray) / len(fearArray)
            surprise = reduce(lambda x, y: x + y, surpriseArray) / len(surpriseArray)
            trust = reduce(lambda x, y: x + y, trustArray) / len(trustArray)
            emotions = [joy, anticipation, sadness, disgust, anger, fear, surprise, trust]
            normemotions = [int(round((float(i)/max(emotions))*100)) for i in emotions]
            emotiondict = {'joy': normemotions[0], 'anticipation': normemotions[1], 'sadness': normemotions[2], 'disgust': normemotions[3], 'anger': normemotions[4], 'fear': normemotions[5], 'surprise': normemotions[6], 'trust': normemotions[7]}
        
            namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="STE" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
            uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="STE" RETURN b.name, count(b)').data()            
            rdict = {"relatedflows":namedict, "upphases": uppDict, "emotionlandscape":emotiondict}
    
    return (json.dumps(rdict))
