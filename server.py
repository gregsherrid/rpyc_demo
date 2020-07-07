from flask import Flask, jsonify
app = Flask(__name__)

@app.route('/')
def hello_world():
	return 'Hello, RPC Demo!'

@app.route("/single")
def single():
	return jsonify({
		"text": "This is one RPC call!"
	})

if __name__ == "__main__":
	app.run(debug=True)