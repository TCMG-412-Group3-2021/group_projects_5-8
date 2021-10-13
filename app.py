from flask import Flask, jsonify
import hashlib

app = Flask(__name__)

@app.route("/")
def hello_and_welcome():
    return "Howdy! Welcome to Group 3's API for TCMG 412."

@app.route('/md5/<string:helloworld>')
def MD5(helloworld):

	hash_obj = hashlib.md5(helloworld.encode())
	return jsonify(input=helloworld, output=hash_obj.hexdigest())

if __name__ == "__main__":
    app.run(debug=True)