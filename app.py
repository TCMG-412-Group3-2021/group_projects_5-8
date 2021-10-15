from flask import Flask, json, jsonify
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_and_welcome():
    return jsonify(input='Howdy!', output= 'Welcome to Group 3s API for TCMG 412.')

@app.route('/md5/<string:helloworld>')
def MD5(helloworld):

	hash_obj = hashlib.md5(helloworld.encode())
	return jsonify(input=helloworld, output=hash_obj.hexdigest())

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



if __name__ == "__main__":
    app.run(debug=True)
    app.run(host='0.0.0.0', port = 5000)