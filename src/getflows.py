from py2neo import Graph
import json

graphURL = 'http://hobby-ipadfcfgpodkgbkedbggakbl.dbs.graphenedb.com:24789'
graphUser = 'rheauser'
graphPass = 'b.tvYI5zZ7SWCQ.l04N5jzsNkbFCzFf'

g = Graph(graphURL, user=graphUser, password=graphPass)




def getflowdata(d):
    
    #d => get page string from json
    t = d['title']
    rdict = []
    if(t == "PTI"):
        namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="PTI" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        
        uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="PTI" RETURN b.name, count(b)').data()            
        rdict = {"relatedflows":namedict, "upphases": uppDict}
        #"up":upcount, "keywords":keywlist, 
    
    if(t == "OFC"):
        namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="OFC" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        
        uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="OFC" RETURN b.name, count(b)').data()            
        rdict = {"relatedflows":namedict, "upphases": uppDict}
    
    if(t == "FTC"):
            namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="FTC" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        
            uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="FTC" RETURN b.name, count(b)').data()            
            rdict = {"relatedflows":namedict, "upphases": uppDict}
    
    if(t == "STE"):
            namedict = g.run('MATCH (n:Flow)-[r]->(u:CoreFlow)WHERE u.cf_id="STE" RETURN n.title, n.doc_id, n.description, n.referenceURL').data()
        
            uppDict = g.run('MATCH (n:CoreFlow) -[x:HOLDSFLOW]-> (r:Flow) -[y:RELEVANTFOR]->(b:UPLCPhase) WHERE n.cf_id="STE" RETURN b.name, count(b)').data()            
            rdict = {"relatedflows":namedict, "upphases": uppDict}
    
    return (json.dumps(rdict))