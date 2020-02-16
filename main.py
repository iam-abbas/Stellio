from amadeus import Client, ResponseError
import json
from flask import Flask, render_template, request 
import iso8601
import twilio.rest

app = Flask(__name__)

def getDuration(t1, t2):
    t1 = iso8601.parse_date(t1)
    t2 = iso8601.parse_date(t2)
    diff = t2-t1
    days, seconds = diff.days, diff.seconds
    hours = days * 24 + seconds // 3600
    minutes = (seconds % 3600) // 60
    return [str(hours)+"H "+str(minutes)+"M"]

def dateWords(d):
    return str(iso8601.parse_date(d).strftime('%A %d %B %Y')).title()

amadeus = Client(
    client_id='w6OWO18wAHAhSOKHOaxZczm8DAzfedIv',
    client_secret='Z3e8Ax7ACNgjWFGD'
)

iata_codes = {
    'LAS': 'Las Vegas',
    'ORD': 'Chicago',
    'JFK': 'New York',
    'SFO': 'San Francisco',
    'DEN': 'Denver',
    'SLC': 'Salt Lake City',
    'LAX': 'Los Angles'
}
@app.route('/search', methods=['GET', 'POST'])
def flight_search():
    fromad = request.args.get("from")
    to = request.args.get("to")
    onDate = request.args.get("date")
    adults = request.args.get("adults")

    response = amadeus.shopping.flight_offers_search.get(originLocationCode=fromad, destinationLocationCode=to, departureDate=onDate, adults=adults)
    return render_template("index.html", len = len(response.data), flights = response.data, codes=iata_codes, getDate = iso8601.parse_date, getDuration=getDuration, dateWords=dateWords, leng=len)

@app.route('/flights')
def landing():
    return render_template("land.html")

@app.route('/map')
def maps():
    return render_template("map.html")

@app.route('/')
def index():
    return render_template("main.html")
@app.route('/tours1')
def tours():
    return render_template("tours.html")
@app.route('/tours')
def tour():
    return render_template("tours1.html")

@app.route('/food')
def food():
    return render_template("food.html")

@app.route('/sms', methods=['GET'])
def sms():
    typef = request.args.get("type")
    namef = request.args.get("name")
    addf = request.args.get("address")
    cno = request.args.get("cno")
    # client credentials are read from TWILIO_ACCOUNT_SID and AUTH_TOKEN
    account_sid = 'ACc968f427b12e6e1251e2ff7ab918e408' # Found on Twilio Console Dashboard
    auth_token = 'dced10d6c48c2a43d89c3ee30f50675c'
    clnt = twilio.rest.Client(account_sid, auth_token)

# this is the Twilio sandbox testing number
    from_whatsapp_number='whatsapp:+14155238886'
# replace this number with your own WhatsApp Messaging number
    to_whatsapp_number='whatsapp:+15102169073'

    clnt.messages.create(body='Hey I have some '+namef+' ('+typef+') '+'available for free at '+addf+' You can call us at '+cno,
                       from_=from_whatsapp_number,
                       to=to_whatsapp_number)
    return '''<script>window.location.replace("/");</script>'''


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)