from flask import Flask, jsonify, request
import json
import datetime

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	# POST method.
	if (request.method == 'POST'):
		post_json = request.get_json()

		# Write json to file.
		with open('output.txt', 'w') as outfile:
			json.dump(post_json, outfile)

		data = {}
		
		# Read data from file.
		with open('output.txt') as json_file:
			data = json.load(json_file)

		# Return the new data, indicating the POST was successful.
		return jsonify({'result' : data}), 201
	# GET method.
	else:
		data = {}
		
		# Read data from file.
		with open('output.txt') as json_file:
			data = json.load(json_file)

		return jsonify({'result' : data})

if __name__ == '__main__':
    app.run(debug=True)