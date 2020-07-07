import rpyc
from IPython import embed
import time

answer_service = rpyc.connect("localhost", 50001)
prime_service = rpyc.connect("localhost", 50002)

print("\n --- Getting the answer ---")
print(answer_service.root.get_answer())
print("Actually:", answer_service.root.the_real_answer_though)

print("\n --- Getting primes ---")
print("Testing:", prime_service.root.good_prime)
print("12:", prime_service.root.primes(12))
print("81:", prime_service.root.primes(81))
print("102213:", prime_service.root.primes(102213))
print("120317:", prime_service.root.primes(120317))

print("\n --- Getting primes aysnc... ---")
print("12929301020229321282823")
async_primes = rpyc.async_(prime_service.root.primes)
pending_primes = async_primes(12929301020229321282823)

start_time = time.time()
while not pending_primes.ready:
	waited = round(time.time() - start_time, 3)
	print("Ready?", pending_primes.ready, waited)
	time.sleep(0.25)

waited = round(time.time() - start_time, 3)
print("Done!", waited)

print("Result:", pending_primes.value)

print("\n --- Done ---")
