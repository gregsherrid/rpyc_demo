import rpyc

class PrimeService(rpyc.Service):
	def on_connect(self, conn):
		pass

	def on_disconnect(self, conn):
		pass

	def exposed_primes(self, n):
		# Thanks @ Daniel
		# https://stackoverflow.com/a/16996439/4557470
		primfac = []
		d = 2
		while d*d <= n:
			while (n % d) == 0:
				primfac.append(d)  # supposing you want multiple factors repeated
				n //= d
			d += 1

		if n > 1:
		   primfac.append(n)

		return primfac

	exposed_good_prime = 53


if __name__ == "__main__":
	from rpyc.utils.server import ThreadedServer
	t = ThreadedServer(PrimeService, port=50002)
	t.start()

