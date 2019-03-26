#!/usr/bin/env python

from flask import Flask, jsonify, request, send_from_directory
import subprocess
import json

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route("/")
def hello():
	proc = subprocess.Popen([
		'python3', 'detect.py',
		# Set parameters; example: `param=argument` or just `option`.
		'default'
		], 
		stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

	# Return file contents of `output.txt`.
	return send_from_directory('', 'output.txt')

if __name__ == '__main__':
    app.run(debug=True)