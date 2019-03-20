#!/usr/bin/env python

from flask import Flask, jsonify
import subprocess

app = Flask(__name__)

@app.route("/")
def hello():
	proc = subprocess.Popen([
		'python', 'getdata.py',
		# Set parameters; example: param=argument.
		'test=Hello from flasky.py',
		'param2=argument2',
		'nothing'
		], 
		stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
	result = proc.communicate()[0].decode('utf-8')

	return jsonify({"about": result})

if __name__ == '__main__':
    app.run(debug=True)