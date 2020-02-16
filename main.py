from amadeus import Client, ResponseError
import json
from flask import Flask, render_template, request 
import iso8601

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
@app.route('/tours')
def tours():
    return render_template("tours.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, threaded=True, debug=True)