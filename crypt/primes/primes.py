from composite_primality import composite_primality
import random

def set_seed(seed):
  random.seed(seed)

def gen_prime(precision, seed):
  # Set the random number seed
  if seed is not None:
    set_seed(seed)
    
  digits = precision - 1  # Reduce the power by 1
  while True:
    # Generate a random number between the lower bound and upper bound of numbers
    # where the precision matches
    rand_num = random.randrange(10 ** digits,  (10 ** (digits + 1)) - 1, 1)
    #rand_num = prime_gen(digits)
    if composite_primality(rand_num):
      return rand_num
      
def get_coprime(prime1, prime2):
  return prime1 * prime2