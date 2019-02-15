from flask import Flask
from waitress import serve
import requests
import random

app = Flask(__name__)


@app.route('/', methods=['GET'])
def get_stop():
	r = requests.get('https://mcb-api.herokuapp.com/get_all_bus_stops')
	quotes = r.json()
	return random.choice(quotes)['quotes']

if __name__ == '__main__':
	serve(app, host='0.0.0.0', port=5000)
