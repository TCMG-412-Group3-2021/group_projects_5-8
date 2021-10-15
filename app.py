from flask import Flask, json, jsonify, request, Response
import hashlib



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

@app.route('/slack-alert/<string:msg>')
def slack(msg):
	SLACK_URL = 'https://hooks.slack.com/services/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'
    
	data = { 'text': msg }
    
	resp = requests.post(SLACK_URL, json=data)
	
	if resp.status_code == 200:
		result = True
        mesg = "Message successfully posted to Slack channel"
    
	else:
        result = False
        mesg = "There was a problem posting to the Slack channel (HTTP response: " + str(resp.status_code) + ")."

    return jsonify(
        input=msg,
        message=mesg,
        output=result
    ), 200 if resp.status_code==200 else 400

if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port = 5000)