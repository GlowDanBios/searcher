from flask import Flask, render_template, request
from pymongo import MongoClient
from bs4 import BeautifulSoup
from pprint import pprint

app = Flask(__name__)

client = MongoClient('mongodb+srv://hhsl:As123456@mempedia-ptiit.mongodb.net/test?retryWrites=true')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/results', methods=['POST'])
def results():
    with client:
        db = client.sites
        sites = db.indexes
        db.indexes.create_index([('text', 'text')])
    req = request.form['req']
    links = []
    results = sites.find({'$text': {'$search': req}}, {'link': True, 'text': True})
    for resul in results:
        if resul['link'] not in links:
            links.append(resul['link'])
    return render_template('results.html', data=list(links))


app.run(debug=True, port=8080)
