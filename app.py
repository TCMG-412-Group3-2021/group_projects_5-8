from flask import Flask, json, jsonify, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
import hashlib

load_dotenv()

app = Flask(__name__)

@app.route("/")
def hello_and_welcome():
    return jsonify(input='Howdy!', output= 'Welcome to Group 3s API for TCMG 412.')

@app.route('/md5/<string:random>')
def MD5(random):

	hash_obj = hashlib.md5(random.encode())
	return jsonify(input=random, output=hash_obj.hexdigest())

@app.route('/factorial/<int:n>')
def Factorial(n):
	n = int(n)

	fact = 1
	if(n < 0):
		return f"{n} is not a positive value"
	elif(n == 0):
		return jsonify(input=n, output=1)
	else:
		for i in range(1, n+1):
			fact = fact*i
		return jsonify(input=n, output=fact)

slack_token = os.environ["SLACK_BOT_TOKEN"]
print(os.environ["SLACK_BOT_TOKEN"])
client = WebClient(token=slack_token)

@app.route('/slack-alert/<string:msg>')
def slack(msg):
	try:
		response = client.chat_postMessage(
			channel="C011KJWHA22",
			text=msg
		)
		print("RESPONSE:", response)
		return jsonify(
			input=msg,
			message=msg,
			output= "Message was successfully sent in slack" if response['ok'] else ''
		), 200 if response['ok'] else 400
	except SlackApiError as e:
		assert e.response["error"]
		return jsonify(
			input=msg,
			message=msg,
			output=e.response["error"]
		)
	

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port = 80)
