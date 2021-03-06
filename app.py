from logging import error
from flask import Flask, json, jsonify, request, Response
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from dotenv import load_dotenv
import os
import hashlib
import redis
from redis import RedisError, Redis

r = redis.StrictRedis(host='127.0.0.1', port=6379)
r.set('foo', 'bar')
r.get('foo')


load_dotenv()

app = Flask(__name__)

@app.route('/keyval', methods=['POST'])
def post():
    # First check for a valid JSON payload
    try:
        payload = request.get_json()
        print(request)
        k = payload["key"]
        v = payload["value"]
    except:
        print('payload:', payload)
        return jsonify(result=False, error="Invalid request (i.e., invalid JSON)" ), 400
    
    y = f"key is {k} and the value is {v}"

    if r.get(k): #if key already exists in redis
        return jsonify(key=k, value=v, command=y, result=False, error="Key already exists"), 409
    elif y == RedisError: #if the payload is bad, check
        return jsonify(key=k, value=v, command=y, result=False, error="Invalid request (i.e., invalid JSON)"), 400
    else: #create the keyval in redis r.set
        r.set(k,v)
        return jsonify(key=k, value=v, command=y, result=True, error=""), 200

@app.route('/keyval', methods=['PUT'])
def put():
    payload = request.get_json()
    n = payload["value"]
    b = payload["key"]
    z = f"key is {b} and the new value is {n}"

    if r.get(b) == None: #if key does not exist in redis
        return jsonify(key=b, newvalue=n, command=z, result=False, error="Key does not exist"), 404
    elif z == RedisError: #if the payload is bad, check
        return jsonify(key=b, newvalue=n, command=z, result=False, error="Invalid request (i.e., invalid JSON)"), 400
    else: #create the new value in redis with r.set
        r.set(b,n)
        return jsonify(key=b, newvalue=n, command=z, result=True, error=""), 200

@app.route('/keyval/<string:key>', methods=['GET'])
def get_key_value(key):
    keyValueJSON = {
        'key': key,
        'value': None,
        'command': "{} {}".format('RETRIEVE', key),
        'result': False,
        'error': None
    }

    # decoding value from redis
    try:
        stored_value = r.get(key)
    except RedisError:
        keyValueJSON['error'] = "Invalid request (i.e., invalid JSON)"
        return jsonify(keyValueJSON), 400

    # checking to see if the key exists
    if stored_value == None:
        keyValueJSON['error'] = "Key does not exist"
        return jsonify(keyValueJSON), 404
    else:
        keyValueJSON['value'] = stored_value.decode("utf-8")

    keyValueJSON['result'] = True
    return jsonify(keyValueJSON), 200

@app.route('/keyval/<string:key>', methods=['DELETE'])
def delete_key_value(key):
    keyValueJSON = {
        'key': key,
        'value': None,
        'command': "{} {}".format('DELETE', key),
        'result': False,
        'error': None
    }
    # decoding value from redis
    try:
        stored_value = r.get(key)
    except RedisError:
        keyValueJSON['error'] = "Invalid request (i.e., invalid JSON)"
        return jsonify(keyValueJSON), 400

    # checking to see if the key exists
    if stored_value == None:
        keyValueJSON['error'] = "Key does not exist"
        return jsonify(keyValueJSON), 404
    else:
        keyValueJSON['value'] = stored_value.decode("utf-8")

    deleteResponse = r.delete(key)
    if deleteResponse == 1:
        keyValueJSON['result'] = True
        return jsonify(keyValueJSON)
    else:
        keyValueJSON['error'] = f"Invalid request (i.e., invalid JSON)"
        return jsonify(keyValueJSON), 400


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

@app.route('/is-prime/<int:number>')
def is_prime(number):
    isPrime = False
    if number == 2:
        isPrime = True
    if number > 2:
        isPrime = True
        for i in range(2, number):
            if number % i == 0:
                isPrime = False
                break

    if isPrime:
       return jsonify(input=number, output=True)
    else:
       return jsonify(input=number, output=False)

@app.route("/fibonacci/<int:number>")
def calc_fibonacci(number):
    fibonacci = [0]
    c1 = 0
    c2 = 1
    fib = 0
    check = 0

    if number < 0:
        return jsonify(input=number, output=False)
    elif number == 0:
        fibonacci = [0]
    else:
        while check == 0:
            fib = c1 + c2
            c2 = c1
            c1 = fib
            if fib <= number:
                fibonacci.append(fib)
            else:
                check = 1
    return jsonify(input=number, output=fibonacci)
       
	
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
		return jsonify(
			input=msg,
			message=msg,
			output= True if response['ok'] else False
		), 200 if response['ok'] else 400
	except SlackApiError as e:
		assert e.response["error"]
		return jsonify(
			input=msg,
			message=msg,
			output=e.response["error"]
		)
	

if __name__ == "__main__":
    app.run(host='0.0.0.0', port = 80)
