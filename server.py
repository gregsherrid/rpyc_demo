from flask import Flask, jsonify, request
import rpyc
import os, sys
import time

answer_service = rpyc.connect("localhost", 50001)
prime_service = rpyc.connect("localhost", 50002)

app = Flask(__name__)

@app.after_request
def handle_after_request(response):
	sys.stdout.flush()
	return response

@app.route('/')
def hello_world():
	return 'Hello, RPC Demo!'

@app.route("/primes")
def primes():
	n = int(request.args.get('n', 42))
	primes = prime_service.root.primes(n)

	return jsonify({
		"text": "This is one RPC call!",
		"primes": primes
	})

@app.route("/async")
def async_request():
	n = int(request.args.get('n', 42))

	async_primes = rpyc.async_(prime_service.root.primes)
	async_answer = rpyc.async_(answer_service.root.get_answer)

	pending_async_primes = async_primes(n)
	pending_async_answer = async_answer()

	iter_count = 0
	while not (pending_async_primes.ready and pending_async_answer.ready):
		print(pending_async_primes.ready, pending_async_answer.ready, iter_count)
		sys.stdout.flush()

		iter_count += 1
		time.sleep(SLEEP_TIME)

	return jsonify({
		"text": "This was two async RPC calls!",
		"answer": pending_async_answer.value,
		"primes": pending_async_primes.value
	})

SLEEP_TIME = 0.1

if __name__ == "__main__":
	app.run(debug=True)