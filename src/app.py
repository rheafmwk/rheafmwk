import ontologytojson
import analyzeflow
import getflows
import flask
from flask import Flask, request, session, redirect, url_for, render_template, flash
import json

application = Flask(__name__)

@application.route('/', methods=['GET'])
def index():
    return flask.render_template("index.html")

@application.route('/flowtemplate', methods=['GET'])
def flowtemplate():
    return flask.render_template("flowtemp.html")
    
    
@application.route('/ontologyview', methods=['GET'])
def ontologyview():
    return flask.render_template("ontologyview.html")
    
@application.route('/ontologyvisualization', methods=['GET'])
def ontologyvisualization():
    return flask.render_template("ontologyexplorer.html")

@application.route('/literature', methods=['GET'])
def literature():
    return flask.render_template("literatureview.html")
    
@application.route('/guideline', methods=['GET'])
def guideline():
    return flask.render_template("guidelineview.html")
    
@application.route('/pti', methods=['GET'])
def pti():
    return flask.render_template("prototypeteamidentity.html")

@application.route('/ofc', methods=['GET'])
def ofc():
    return flask.render_template("organizeforcomplexity.html") 

@application.route('/ftc', methods=['GET'])
def ftc():
    return flask.render_template("facilitateteamcohesion.html")

@application.route('/ste', methods=['GET'])
def ste():
    return flask.render_template("structurefortaskeffectiveness.html")    
    
@application.route("/ontologydata")
def ontologydata():
    return ontologytojson.getontologydata()

@application.route("/node/<nodename>", methods=['GET'])
def node(nodename):
    myname = nodename.split(".")[-1]
    if nodename.startswith("solarbird.flow"):
        return ontologytojson.getflowdata(myname)
    elif nodename.startswith("solarbird.coreflow"):
        return ontologytojson.getcfdata(myname)
    elif nodename.startswith("solarbird.behaviour"):
        return ontologytojson.getbehaviourdata(myname)
    elif nodename.startswith("solarbird.risk"):
        return ontologytojson.getriskdata(myname)
    elif nodename.startswith("solarbird.upphase"):
        return ontologytojson.getupdata(myname)
    elif nodename.startswith("solarbird.emotion"):
        return ontologytojson.getemotiondata(myname)


@application.route('/analyze_flow', methods=['POST'])
def analyze_flow():
    content = request.get_json(silent=True)
    return analyzeflow.getanalysis(content)

@application.route('/getflows', methods=['POST'])
def get_flows():
    content = request.get_json(silent=True)
    return getflows.getflowdata(content)
