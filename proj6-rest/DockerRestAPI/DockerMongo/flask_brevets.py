"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config

import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()
app.secret_key = CONFIG.SECRET_KEY
client = MongoClient(os.environ['DB_PORT_27017_TCP_ADDR'], 27017)
db = client.calcdb
###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    flask.session['linkback'] = flask.url_for("index")
    return flask.render_template('404.html'), 404


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    # FIXME: These probably aren't the right open and close times
    # and brevets may be longer than 200km
    bv = request.args.get('bv', type=int)
    dttm = request.args.get('dttm', type=str)
        
    if (isinstance(km, float) and not(km < 0)):
        if (km < (bv*1.05)) :
            open_time = acp_times.open_time(km, bv, dttm)
            close_time = acp_times.close_time(km, bv, dttm)
            if (open_time != -1):
                result = {"open": open_time, "close": close_time}
            else:
                result = { "errmsg": "Exceeded Distance Limit!" }
        else:
            result = { "errmsg": "Too Long Distance!" }
    else:
        result = { "errmsg": "Invalid Distance!" }

    return flask.jsonify(result=result)


#############

@app.route('/sbmt', methods=['POST'])
def sbmt():
    db.calcdb.delete_many({})
    miles_doc = request.form.getlist("miles")
    km_doc = request.form.getlist("km")
    location_doc = request.form.getlist("location")
    open_doc = request.form.getlist("open")
    close_doc = request.form.getlist("close")
    
    for row in range(len(open_doc)):
        if (open_doc[row] != ""):
            datalist = { "miles": miles_doc[row], "km": float(km_doc[row]), "location": location_doc[row],
                         "open": open_doc[row], "close": close_doc[row] }
            db.calcdb.insert_one(datalist)
            
    return redirect(url_for('index'))

@app.route('/dsply')
def dsply():
    _items = db.calcdb.find().sort("km")
    items = [item for item in _items]
    return render_template('dsply.html', items=items)

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")

