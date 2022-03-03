import primes

precision = 5
seed = 1234

print(primes.gen_prime(precision, None))
print(primes.gen_prime(precision, seed))
print(primes.get_coprime(primes.gen_prime(precision, None), primes.gen_prime(precision, None)))