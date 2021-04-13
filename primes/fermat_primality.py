# Basic fermat primality test for prime numbers
#
# This will probably get integrated into a composite primality test.

import random

def fermat_primality(randPrime):
  
  if (randPrime % 2 == 0 and randPrime):
    return False
    
  upper_bound = randPrime - 1
  witness = random.randrange(1, upper_bound, 1)
  
  # Do five iterations to weed out pseudoprimes
  isPrime = False
  
  for i in 40:
    if (witness ** (randPrime - 1) % randPrime == 1):
      isPrime = True
    else: isPrime = False
    
    witness = random.randrange(1, upper_bound, 1)
  
  return isPrime
